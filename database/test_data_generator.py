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

def generate_managers(cursor, num_managers=30): # REQUEST: 30 managers
    """
    Generates a hierarchy of managers.
    Schema: Manager(MID, Name, Salary, Contact, Supervisor)
    """
    print(f"Generating {num_managers} Managers...")
    manager_ids = []

    # 1. Create the Executive Officer (Supervisor is NULL)
    exec_name = fake.name()
    cursor.execute(
        "INSERT INTO Manager (Name, Salary, Contact, Supervisor) VALUES (?, ?, ?, ?)",
        (exec_name, random.randint(80000, 120000), int(fake.msisdn()[:8]), None)
    )
    exec_id = cursor.lastrowid
    manager_ids.append(exec_id)
    # print(f"  - Executive created: {exec_name} (ID: {exec_id})")

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

def generate_workers(cursor, manager_ids, num_workers=100): # REQUEST: 100 workers
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

def generate_locations(cursor, manager_ids, num_locations=5): # REQUEST: 5 locations
    """
    Generates locations. 
    Schema: Location(Name, Facility, Supervisor)
    """
    print(f"Generating {num_locations} Locations...")
    location_names = []
    
    # Mix of room codes and descriptive names
    prefixes = ["PQ", "QT", "Z", "N", "X", "Block "]
    facilities = ["Corridor", "Laboratory", "Washroom", "Classroom", "Lobby", "Gate", "Square", "Swimming Pool", "Library", "Garden", "Carpark"]
    
    count = 0
    while count < num_locations:
        prefix = random.choice(prefixes)
        if prefix == "Block ":
            name = f"{prefix}{random.choice(['A', 'B', 'C', 'L', 'V', 'X', 'Y', 'Z'])}"
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
            count += 1
        except sqlite3.IntegrityError:
            # Skip duplicate names generated by random chance
            continue
            
    return location_names

def generate_companies(cursor, num_companies=10): # REQUEST: 10 companies
    """
    Generates outsourcing companies.
    Schema: Company(CompanyID, Name, Address, Contact)
    """
    print(f"Generating {num_companies} Companies...")
    company_ids = []
    company_suffixes = ["Services Ltd.", "Facility Mgmt", "Gardening Co.", "Engineering", "Cleaners"]
    
    for _ in range(num_companies):
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
    REQUEST:
    - 50 more Activity
    - 50 more tasks (approx 1 per activity)
    - 10 more TaskChemicals
    - 20 holdIN
    - 10 workOn
    - 30 more assigned
    """
    print("Generating Activities and Details...")
    
    actions = ["Cleaning", "Inspection", "Repair", "Maintenance", "Deep Clean", "Drill"]
    
    # We need 50 Activities
    generated_activities = []
    
    for _ in range(50): # REQUEST: 50 more Activity
        act_name = f"{random.choice(actions)} of {fake.word()}"
        start_date = fake.date_this_year()
        if random.random() < 0.2:
            end_date = start_date
        else:
            end_date = start_date + timedelta(days=random.randint(1, 10))
            
        cursor.execute(
            "INSERT INTO Activity (Name, startDate, endDate) VALUES (?, ?, ?)",
            (act_name, start_date.isoformat(), end_date.isoformat())
        )
        aid = cursor.lastrowid
        generated_activities.append(aid)

    # REQUEST: 20 HoldIn (Assign 20 of the 50 activities to locations)
    # We shuffle activities to pick random ones
    activities_for_holdin = random.sample(generated_activities, min(20, len(generated_activities)))
    if location_names:
        for aid in activities_for_holdin:
            loc_name = random.choice(location_names)
            try:
                cursor.execute(
                    "INSERT INTO HoldIn (AID, LocationName) VALUES (?, ?)",
                    (aid, loc_name)
                )
            except sqlite3.IntegrityError:
                pass # Should not happen if logic is correct, but safe to ignore

    # REQUEST: 10 WorkOn (Assign 10 of the 50 activities to companies)
    # We pick random ones that might or might not overlap with HoldIn (schema allows)
    activities_for_workon = random.sample(generated_activities, min(10, len(generated_activities)))
    if company_ids:
        for aid in activities_for_workon:
            cid = random.choice(company_ids)
            payment = random.randint(10000, 50000)
            quarter = f"2025-Q{random.randint(1, 4)}"
            cursor.execute(
                "INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (?, ?, ?, ?)",
                (aid, cid, payment, quarter)
            )

    # REQUEST: 50 more tasks
    # We will assign 1 task to each of the 50 activities to meet the "50 tasks" requirement simply
    task_list = [] # Store (aid, task_name) for later use
    
    for aid in generated_activities:
        task_verbs = ["Sweep", "Mop", "Scrub", "Inspect", "Repair", "Replace", "Vacuum", "Spray"]
        task_name = f"{random.choice(task_verbs)} {fake.word()} {random.randint(1, 100)}" 
        equipment = random.choice(["Standard tools", "Scrubber", "Pressure washer", "Ladder", "Inspection tools", "Vacuum cleaner"])
        
        cursor.execute(
            "INSERT INTO Task (AID, Name, Equipment) VALUES (?, ?, ?)",
            (aid, task_name, equipment)
        )
        task_list.append((aid, task_name))

    # REQUEST: 10 more TaskChemicals
    # Pick 10 random tasks to assign chemicals to
    tasks_for_chemicals = random.sample(task_list, min(10, len(task_list)))
    possible_chems = ["Bleach", "Descaler", "Floor wax", "Degreaser", "Anti-mold spray", "Insecticide", "Solvent"]
    
    for aid, task_name in tasks_for_chemicals:
        chem = random.choice(possible_chems)
        cursor.execute(
            "INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (?, ?, ?)",
            (aid, task_name, chem)
        )

    # REQUEST: 30 more assigned
    # Assign workers to 30 tasks
    tasks_for_assignment = random.sample(task_list, min(30, len(task_list)))
    if worker_ids:
        for aid, task_name in tasks_for_assignment:
            wid = random.choice(worker_ids)
            cursor.execute(
                "INSERT INTO Assigned (WID, AID, TaskName) VALUES (?, ?, ?)",
                (wid, aid, task_name)
            )

def main():
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            clear_data(cursor)
            
            manager_ids = generate_managers(cursor, num_managers=30)
            worker_ids = generate_workers(cursor, manager_ids, num_workers=100)
            location_names = generate_locations(cursor, manager_ids, num_locations=5)
            company_ids = generate_companies(cursor, num_companies=10)
            
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
