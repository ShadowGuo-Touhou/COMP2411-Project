import sqlite3
import os
from . import config

def Create_database(db_name="test.db"):
    db_name = config.DB_NAME

    db_exists = os.path.exists(db_name)
    if db_exists:
        print(f"'{db_name}' already exists.")
    else:
        print(f"Creating new database '{db_name}'...")

    # initalize the database
    schema_sql = """
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS Manager (
        MID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Contact INTEGER NOT NULL,
        Supervisor INTEGER,
        FOREIGN KEY (Supervisor) REFERENCES Manager(MID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    ) STRICT;

    CREATE TABLE IF NOT EXISTS Worker (
        WID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Contact INTEGER NOT NULL,
        Supervisor INTEGER,
        FOREIGN KEY (Supervisor) REFERENCES Manager(MID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    ) STRICT;

    CREATE TABLE IF NOT EXISTS Location (
        Name TEXT PRIMARY KEY,
        Facility TEXT,
        Supervisor INTEGER,
        FOREIGN KEY (Supervisor) REFERENCES Manager(MID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    ) STRICT;

    CREATE TABLE IF NOT EXISTS Activity (
        AID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        startDate TEXT,
        endDate TEXT,
        CHECK (startDate IS NULL OR endDate IS NULL OR endDate>=startDate)
    ) STRICT;

    CREATE TABLE IF NOT EXISTS Company (
        CompanyID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Address TEXT NOT NULL,
        Contact INTEGER NOT NULL
    ) STRICT;

    CREATE TABLE IF NOT EXISTS Task (
        AID INTEGER NOT NULL,
        Name TEXT NOT NULL,
        Equipment TEXT,
        Chemicals TEXT,
        PRIMARY KEY (AID, Name),
        FOREIGN KEY (AID) REFERENCES Activity(AID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        DEFERRABLE INITIALLY DEFERRED
    );

    CREATE TABLE IF NOT EXISTS Assigned (
        WID INTEGER NOT NULL,
        AID INTEGER NOT NULL,
        TaskName TEXT NOT NULL,
        PRIMARY KEY (WID, AID, TaskName),
        FOREIGN KEY (WID) REFERENCES Worker(WID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
        FOREIGN KEY (AID, TaskName) REFERENCES Task(AID, Name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        DEFERRABLE INITIALLY DEFERRED
    );
    """

    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            
            cursor.executescript(schema_sql)
            
            print("Schema executed successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")