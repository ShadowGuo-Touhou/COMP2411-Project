from sqlprocessor import SQLProcessor

# Connects to data.db by default
db = SQLProcessor() 

# Execute the SQL file that creates tables and inserts data
# Adjust path if testdata.sql is in database/ folder
print("Initializing database from SQL file...")
success = db.readFile("database/testdata.sql") 

if success:
    print("Database successfully initialized!")
else:
    print("Failed to initialize database.")
