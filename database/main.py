from create_database import Create_database 
import test_data_generator

if __name__ == "__main__":
    try:
        Create_database()
        test_data_generator.main()
    except:
        print("Database already exists")
        
    
