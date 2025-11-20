import sqlite3
import random
from datetime import datetime, timedelta
from faker import Faker
from . import config

# Initialize Faker
fake = Faker()

db_name = config.DB_NAME

def get_db_connection():
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def clear_data(cursor):
    """Deletes existing data in reverse order of dependencies."""
    print("Clearing existing data...")
    tables = ["Assigned", "Task", "Activity", "Location", "Worker", "Manager", "Company"]
    for table in tables:
        cursor.execute(f"DELETE FROM {table}")

def generate_managers(cursor, num_mid_managers=10):
    """
    Generates managers.
    According to PDF: 
    1. Executive Officer (Supervisor is NULL).
    2. Mid-level Managers (Supervisor is Executive Officer).
    """
    print("Generating Managers...")
    
    # 1. Create the Executive Officer (The Big Boss)
    # MID, Name, Salary, Contact, Supervisor
    exec_name = fake.name()
    cursor.execute(
        "INSERT INTO Manager (Name, Salary, Contact, Supervisor) VALUES (?, ?, ?, ?)",
        (exec_name, 150000, int(fake.msisdn()[:10]), None)
    )
    exec_id = cursor.lastrowid
    print(f"  - Executive Officer created: {exec_name} (MID: {exec_id})")

    # 2. Create Mid-level Managers
    manager_ids = []
    for _ in range(num_mid_managers):
        name = fake.name()
        salary = random.randint(50000, 90000)
        contact = int(fake.msisdn()[:10])
        
        cursor.execute(
            "INSERT INTO Manager (Name, Salary, Contact, Supervisor) VALUES (?, ?, ?, ?)",
            (name, salary, contact, exec_id)
        )
        manager_ids.append(cursor.lastrowid)
    
    return manager_ids

def generate_workers(cursor, manager_ids, num_workers=50):
    """
    Generates workers.
    According to PDF: Workers are supervised by Mid-level Managers.
    """
    print(f"Generating {num_workers} Workers...")
    worker_ids = []
    
    for _ in range(num_workers):
        name = fake.name()
        salary = random.randint(15000, 35000)
        contact = int(fake.msisdn()[:10])
        # Assign a random mid-level manager as supervisor
        supervisor_id = random.choice(manager_ids)
        
        cursor.execute(
            "INSERT INTO Worker (Name, Salary, Contact, Supervisor) VALUES (?, ?, ?, ?)",
            (name, salary, contact, supervisor_id)
        )
        worker_ids.append(cursor.lastrowid)
        
    return worker_ids

def generate_locations(cursor, manager_ids):
    """
    Generates locations (Campus context).
    According to PDF: Each location has a Supervisor (Manager).
    """
    print("Generating Locations...")
    # PolyU/Campus style names
    locations = [
        ("Block Z", "Administrative Building"),
        ("Block A", "Engineering Faculty"),
        ("Block V", "Jockey Club Innovation Tower"),
        ("Library", "Main Library"),
        ("Canteen", "Student Canteen"),
        ("Podium", "Public Area"),
        ("Room 101", "Lecture Hall"),
        ("Lab 404", "Computer Laboratory"),
        ("Gym", "Sports Center"),
        ("Main Gate", "Entrance")
    ]
    
    for name, facility in locations:
        supervisor_id = random.choice(manager_ids)
        try:
            cursor.execute(
                "INSERT INTO Location (Name, Facility, Supervisor) VALUES (?, ?, ?)",
                (name, facility, supervisor_id)
            )
        except sqlite3.IntegrityError:
            pass # Skip duplicates if re-running without clearing

def generate_companies(cursor):
    """Generates outsourcing companies."""
    print("Generating Outsourcing Companies...")
    companies = ["CleanCo", "FixItFast", "CampusSecure", "GreenGardens", "TechSupport Pro"]
    
    for comp_name in companies:
        address = fake.address().replace("\n", ", ")
        contact = int(fake.msisdn()[:10])
        cursor.execute(
            "INSERT INTO Company (Name, Address, Contact) VALUES (?, ?, ?)",
            (comp_name, address, contact)
        )

def generate_activities_and_tasks(cursor, worker_ids):
    """
    Generates Activities, Tasks, and Assigns Workers.
    """
    print("Generating Activities, Tasks, and Assignments...")
    
    activity_types = ["Cleaning", "Renovation", "Maintenance", "Inspection"]
    
    # Generate 15 Activities
    for _ in range(15):
        act_name = f"{random.choice(activity_types)} - {fake.word().capitalize()}"
        
        # Generate dates (ISO-8601)
        start_date_obj = fake.date_this_year()
        # 30% chance of being ongoing (endDate is NULL)
        if random.random() < 0.3:
            end_date_str = None
        else:
            end_date_obj = start_date_obj + timedelta(days=random.randint(1, 14))
            end_date_str = end_date_obj.isoformat()
            
        start_date_str = start_date_obj.isoformat()
        
        cursor.execute(
            "INSERT INTO Activity (Name, startDate, endDate) VALUES (?, ?, ?)",
            (act_name, start_date_str, end_date_str)
        )
        aid = cursor.lastrowid
        
        # Generate 1 to 3 Tasks for this Activity
        num_tasks = random.randint(1, 3)
        for i in range(num_tasks):
            task_name = f"Task {i+1}: {fake.bs()}" # Random business jargon as task name
            equipment = random.choice(["Ladder", "Drill", "Mop", "Vacuum", "Wrench", None])
            chemicals = random.choice(["Bleach", "Ammonia", "Solvent", None])
            
            cursor.execute(
                "INSERT INTO Task (AID, Name, Equipment, Chemicals) VALUES (?, ?, ?, ?)",
                (aid, task_name, equipment, chemicals)
            )
            
            # Assign 1 to 4 Workers to this Task
            # Constraint: (WID, AID, TaskName) is PK
            num_assigned = random.randint(1, 4)
            assigned_workers = random.sample(worker_ids, num_assigned)
            
            for wid in assigned_workers:
                cursor.execute(
                    "INSERT INTO Assigned (WID, AID, TaskName) VALUES (?, ?, ?)",
                    (wid, aid, task_name)
                )

def main():
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # 1. Clear old data
            clear_data(cursor)
            
            # 2. Managers (Executive + Mid-level)
            manager_ids = generate_managers(cursor, num_mid_managers=8)
            
            # 3. Workers
            worker_ids = generate_workers(cursor, manager_ids, num_workers=40)
            
            # 4. Locations
            generate_locations(cursor, manager_ids)
            
            # 5. Companies
            generate_companies(cursor)
            
            # 6. Activities, Tasks, and Assignments
            generate_activities_and_tasks(cursor, worker_ids)
            
            conn.commit()
            print("\nSUCCESS: Database populated with testing data.")
            
    except sqlite3.Error as e:
        print(f"\nERROR: An error occurred: {e}")

if __name__ == "__main__":
    main()