import sqlite3
import random
from datetime import datetime, timedelta
from faker import Faker
import os
import sys

# Try to import config, handling different execution contexts
try:
    from . import config
except ImportError:
    try:
        import config
    except ImportError:
        # Fallback if config not found, assuming standard name
        class Config:
            DB_NAME = "data.db"
        config = Config()

# Initialize Faker
fake = Faker()

def get_db_connection():
    """
    Establishes a connection to the database.
    """
    # If the script is run from database/ directory, adjust path to find data.db in root
    db_path = config.DB_NAME
    if not os.path.exists(db_path) and os.path.exists(os.path.join("..", db_path)):
        db_path = os.path.join("..", db_path)
        
    conn = sqlite3.connect(db_path)
    # Enforce foreign key constraints (Critical for the schema)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def clear_data(cursor):
    """
    Deletes existing data in reverse order of dependencies to avoid FK violations.
    Schema Dependencies:
    - Assigned -> Worker, Task
    - TaskChemicals -> Task
    - Task -> Activity
    - WorkOn -> Activity, Company
    - HoldIn -> Activity, Location
    - Activity -> (None)
    - Location -> Manager
    - Worker -> Manager
    - Manager -> Manager (Self-referencing)
    - Company -> (None)
    """
    print("Clearing existing data...")
    # Order matters: Child tables first, then Parent tables
    tables = [
        "Assigned", 
        "TaskChemicals", 
        "Task", 
        "WorkOn", 
        "HoldIn", 
        "Activity", 
        "Location", 
        "Worker", 
        "Manager", 
        "Company"
    ]
    for table in tables:
        try:
            cursor.execute(f"DELETE FROM {table}")
            # Reset auto-increment counters if using SQLite
            try:
                cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table}'")
            except sqlite3.OperationalError:
                pass # sqlite_sequence might not exist or table might not use autoincrement
        except sqlite3.OperationalError as e:
            print(f"Warning: Could not clear table {table}: {e}")

def generate_managers(cursor, num_managers=10):
    """
    Generates a hierarchy of managers.
    Schema: Manager(MID, Name, Salary, Contact, Supervisor)
    """
    print("Generating Managers...")
    manager_ids = []

    # 1. Create the Executive Officer (Supervisor is NULL)
    exec_name = fake.name()
    cursor.execute(
        "INSERT INTO Manager (Name, Salary, Contact, Supervisor) VALUES (?, ?, ?, ?)",
        (exec_name, random.randint(80000, 120000), int(fake.msisdn()[:8]), None)
    )
    exec_id = cursor.lastrowid
    manager_ids.append(exec_id)
    print(f"  - Executive created: {exec_name} (ID: {exec_id})")

    # 2. Create remaining managers reporting to existing managers
    for _ in range(num_managers - 1):
        name = fake.name()
        salary = random.randint(45000, 75000)
        contact = int(fake.msisdn()[:8])
        # Pick a supervisor from those already created (creates a tree structure)
        supervisor_id = random.choice(manager_ids)
        
        cursor.execute(
            "INSERT INTO Manager (Name, Salary, Contact, Supervisor) VALUES (?, ?, ?, ?)",
            (name, salary, contact, supervisor_id)
        )
        manager_ids.append(cursor.lastrowid)
    
    return manager_ids

def generate_workers(cursor, manager_ids, num_workers=30):
    """
    Generates workers assigned to supervisors.
    Schema: Worker(WID, Name, Salary, Contact, Supervisor)
    """
    print(f"Generating {num_workers} Workers...")
    worker_ids = []
    
    for _ in range(num_workers):
        name = fake.name()
        salary = random.randint(15000, 25000)
        contact = int(fake.msisdn()[:8])
        supervisor_id = random.choice(manager_ids)
        
        cursor.execute(
            "INSERT INTO Worker (Name, Salary, Contact, Supervisor) VALUES (?, ?, ?, ?)",
            (name, salary, contact, supervisor_id)
        )
        worker_ids.append(cursor.lastrowid)
        
    return worker_ids

def generate_locations(cursor, manager_ids):
    """
    Generates locations. 
    Schema: Location(Name, Facility, Supervisor)
    """
    print("Generating Locations...")
    location_names = []
    
    # Mix of room codes and descriptive names
    prefixes = ["PQ", "QT", "Z", "N", "X", "Block "]
    facilities = ["Corridor", "Laboratory", "Washroom", "Classroom", "Lobby", "Gate", "Square", "Swimming Pool", "Library", "Garden", "Carpark"]
    
    for _ in range(100):
        prefix = random.choice(prefixes)
        if prefix == "Block ":
            name = f"{prefix}{random.choice(['A', 'B', 'C', 'L', 'V'])}"
        else:
            name = f"{prefix}{random.randint(100, 999)}"
            
        facility = random.choice(facilities)
        supervisor_id = random.choice(manager_ids)
        
        try:
            cursor.execute(
                "INSERT INTO Location (Name, Facility, Supervisor) VALUES (?, ?, ?)",
                (name, facility, supervisor_id)
            )
            location_names.append(name)
        except sqlite3.IntegrityError:
            # Skip duplicate names generated by random chance
            continue
            
    return location_names

def generate_companies(cursor):
    """
    Generates outsourcing companies.
    Schema: Company(CompanyID, Name, Address, Contact)
    """
    print("Generating Companies...")
    company_ids = []
    company_suffixes = ["Services Ltd.", "Facility Mgmt", "Gardening Co.", "Engineering", "Cleaners"]
    
    for _ in range(10):
        name = f"{fake.word().capitalize()}{fake.word().capitalize()} {random.choice(company_suffixes)}"
        address = fake.address().replace("\n", ", ")
        contact = int(fake.msisdn()[:8])
        
        cursor.execute(
            "INSERT INTO Company (Name, Address, Contact) VALUES (?, ?, ?)",
            (name, address, contact)
        )
        company_ids.append(cursor.lastrowid)
    return company_ids

def generate_activities_and_details(cursor, worker_ids, location_names, company_ids):
    """
    Generates Activities and populates dependent tables.
    Schema Covered:
    - Activity(AID, Name, startDate, endDate)
    - HoldIn(AID, LocationName)
    - WorkOn(AID, CompanyID, ContractedPayment, ContractedTime)
    - Task(AID, Name, Equipment)
    - TaskChemicals(AID, TaskName, Chemicals)
    - Assigned(WID, AID, TaskName)
    """
    print("Generating Activities and Tasks...")
    
    actions = ["Cleaning", "Inspection", "Repair", "Maintenance", "Deep Clean", "Drill"]
    
    for _ in range(100): # Increased from 20 to 30 for more data
        # 1. Create Activity
        act_name = f"{random.choice(actions)} of {fake.word()}"
        start_date = fake.date_this_year()
        # Ensure endDate >= startDate as per schema CHECK constraint
        if random.random() < 0.2:
            end_date = start_date
        else:
            end_date = start_date + timedelta(days=random.randint(1, 10))
            
        cursor.execute(
            "INSERT INTO Activity (Name, startDate, endDate) VALUES (?, ?, ?)",
            (act_name, start_date.isoformat(), end_date.isoformat())
        )
        aid = cursor.lastrowid
        
        # 2. HoldIn (Where does this activity happen?)
        # Pick a random location
        if location_names:
            loc_name = random.choice(location_names)
            cursor.execute(
                "INSERT INTO HoldIn (AID, LocationName) VALUES (?, ?)",
                (aid, loc_name)
            )
        
        # 3. WorkOn (Is it outsourced?)
        # 50% chance an activity is outsourced to a company
        if random.random() < 0.5 and company_ids:
            cid = random.choice(company_ids)
            payment = random.randint(10000, 50000)
            quarter = f"2025-Q{random.randint(1, 4)}"
            cursor.execute(
                "INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (?, ?, ?, ?)",
                (aid, cid, payment, quarter)
            )
            
        # 4. Tasks
        num_tasks = random.randint(1, 3)
        for i in range(num_tasks):
            # Task Name must be unique per Activity (PK: AID, Name)
            task_verbs = ["Sweep", "Mop", "Scrub", "Inspect", "Repair", "Replace", "Vacuum", "Spray"]
            task_name = f"{random.choice(task_verbs)} {fake.word()} {i+1}" # Added index to ensure uniqueness within activity
            equipment = random.choice(["Standard tools", "Scrubber", "Pressure washer", "Ladder", "Inspection tools", "Vacuum cleaner"])
            
            cursor.execute(
                "INSERT INTO Task (AID, Name, Equipment) VALUES (?, ?, ?)",
                (aid, task_name, equipment)
            )
            
            # 5. TaskChemicals (FK: AID, TaskName)
            # A task might use 0, 1, or 2 chemicals
            num_chems = random.randint(0, 2)
            possible_chems = ["Bleach", "Descaler", "Floor wax", "Degreaser", "Anti-mold spray", "Insecticide", "Solvent"]
            
            # Ensure unique chemicals per task (PK: AID, TaskName, Chemicals)
            selected_chems = random.sample(possible_chems, num_chems)
            for chem in selected_chems:
                cursor.execute(
                    "INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (?, ?, ?)",
                    (aid, task_name, chem)
                )
                
            # 6. Assigned (Workers) (FK: WID, AID, TaskName)
            # Assign 1 to 3 workers to this specific task
            num_assigned = random.randint(1, 3)
            if worker_ids:
                assigned_workers = random.sample(worker_ids, min(len(worker_ids), num_assigned))
                
                for wid in assigned_workers:
                    cursor.execute(
                        "INSERT INTO Assigned (WID, AID, TaskName) VALUES (?, ?, ?)",
                        (wid, aid, task_name)
                    )

def main():
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            clear_data(cursor)
            
            manager_ids = generate_managers(cursor, num_managers=10)
            worker_ids = generate_workers(cursor, manager_ids, num_workers=40)
            location_names = generate_locations(cursor, manager_ids)
            company_ids = generate_companies(cursor)
            
            generate_activities_and_details(cursor, worker_ids, location_names, company_ids)
            
            conn.commit()
            print("\nSUCCESS: Database populated with testing data following the new schema.")
            
    except sqlite3.Error as e:
        print(f"\nERROR: Database error: {e}")
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
