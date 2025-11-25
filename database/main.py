import os
import sqlite3
import sys

# Add parent directory to sys.path to allow imports if run directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from database import config
    from database import test_data_generator
except ImportError:
    try:
        import config
        import test_data_generator
    except ImportError as e:
        print(f"Critical Error: Could not import config or test_data_generator. Details: {e}")
        sys.exit(1)

def init_schema():
    """
    Initialize the database schema from configuration.sql
    """
    db_name = config.DB_NAME
    
    # Determine correct path to data.db
    # If running from database/ directory, data.db might be in parent or current
    # We prefer the one defined in config, usually root
    if not os.path.exists(db_name) and os.path.exists(os.path.join("..", db_name)):
        db_name = os.path.join("..", db_name)
    
    # Path to configuration.sql
    # Try finding it relative to current script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sql_path = os.path.join(base_dir, "configuration.sql")
    
    if not os.path.exists(sql_path):
        print(f"Error: Could not find configuration.sql at {sql_path}")
        return False
        
    print(f"Initializing schema from {sql_path} into {db_name}...")
    
    try:
        with open(sql_path, 'r', encoding='utf-8') as f:
            schema_sql = f.read()
            
        with sqlite3.connect(db_name) as conn:
            # Enable foreign keys support
            conn.execute("PRAGMA foreign_keys = ON;")
            conn.executescript(schema_sql)
            
        print("Schema initialized successfully.")
        return True
    except Exception as e:
        print(f"Schema initialization failed: {e}")
        return False

if __name__ == "__main__":
    # Remove existing database to ensure clean schema initialization
    if os.path.exists(config.DB_NAME):
        try:
            os.remove(config.DB_NAME)
            print(f"Removed existing {config.DB_NAME}")
        except OSError as e:
            print(f"Error removing {config.DB_NAME}: {e}")

    # First, initialize the schema (creates tables)
    if init_schema():
        print("Generating test data...")
        try:
            # Then, populate with data
            test_data_generator.main()
        except Exception as e:
            print(f"Data generation failed: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("Skipping data generation due to schema initialization failure.")
