import sqlite3 
from . import config

db_name = config.DB_NAME
def getBuilding_fromDB(db_name="test.db"):
    try:
        conn = sqlite3.connect(db_name)
        data = conn.execute("Select Name from Location;")
        return data
    except e:
        print(e)
        print("you lose")