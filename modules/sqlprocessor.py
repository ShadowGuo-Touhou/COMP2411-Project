import sqlite3
import os

class SQLProcessor:
    def __init__(self, db_path="data.db"):
        
        self.db_path = db_path
        self.con = sqlite3.connect(db_path)
        self.con.execute("PRAGMA foreign_keys = ON;")
        self.cur = self.con.cursor()
        
        self.columns = {
            "Manager": ["MID", "Name", "Salary", "Contact", "Supervisor"],
            "Worker": ["WID", "Name", "Salary", "Contact", "Supervisor"],
            "Location": ["Name", "Facility", "Supervisor"],
            "Activity": ["AID", "Name", "startDate", "endDate"],
            "Company": ["CompanyID", "Name", "Address", "Contact"],
            "Task": ["AID", "Name", "Equipment"],
            "TaskChemicals": ["AID", "TaskName", "Chemicals"],
            "Assigned": ["WID", "AID", "TaskName"],
            "HoldIn": ["AID", "LocationName"],
            "WorkOn": ["AID", "CompanyID", "ContractedPayment", "ContactedTime"]
        }
        self.tables = list(self.columns.keys())
        self.harmfulChemicals = ["Acidic descaler","Bleach solution","TNT","NaClO","HCl","Cockroach Insecticide","Rat Poison","X-ray"]

    def execute(self, command, params=None):
        try:
            if params:
                self.cur.execute(command, params)
            else:
                self.cur.execute(command)
            self.con.commit()
            return self.cur
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_all(self, command, params=None):
        cursor = self.execute(command, params)
        if cursor:
            return cursor.fetchall()
        return []

    def getTables(self):
        return self.tables

    def getColumns(self, table):
        return self.columns.get(table, [])

    def readFile(self, filePath):
        if not filePath.endswith('.sql'):
            print("Please give a sql file!")
            return False
        try:
            with open(filePath, 'r', encoding='utf-8') as f:
                sql_script = f.read()
            
            statements = sql_script.split(';')
            for statement in statements:
                statement = statement.strip()
                if statement and statement!="COMMIT":
                    self.execute(statement)
            return True
        except Exception as e:
            print(f"Error reading file: {e}")
            return False
        
    def insert(self, table, data_dict):
        """Insert data into table"""
        if table not in self.columns:
            return False
        columns = self.columns[table]
        placeholders = ','.join(['?' for _ in data_dict])
        columns_str = ','.join(data_dict.keys())
        values = list(data_dict.values())
        
        command = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
        return self.execute(command, values) is not None

    def update(self, table, changes, condition="1=1"):
        """Update data in table"""
        if table not in self.columns:
            return False
        set_clause = ','.join([f"{k}=?" for k in changes.keys()])
        values = list(changes.values())
        
        command = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        return self.execute(command, values) is not None

    def delete(self, table, condition="1=1"):
        """Delete data from table"""
        command = f"DELETE FROM {table} WHERE {condition}"
        return self.execute(command) is not None

    def queryForActivity(self, location, chemicals=None):
        if chemicals is None:
            chemicals = self.harmfulChemicals
        query = """
        SELECT A.AID, A.Name, A.startDate, A.endDate, 
               (SELECT COUNT(*) 
                FROM TaskChemicals TC 
                WHERE TC.AID = A.AID 
                  AND TC.Chemicals IN ({})
               ) AS Harmful_chemicals_count
        FROM Activity A
        JOIN HoldIn H ON A.AID = H.AID
        WHERE H.LocationName = ?
        GROUP BY A.AID, A.Name, A.startDate, A.endDate
        """.format(','.join(['?' for _ in chemicals]))
        
        params = chemicals + [location]
        return self.fetch_all(query, params)

    def queryForActivityWithDate(self, location, startDate, endDate, chemicals=None):
        """Query activities based on location and date range"""
        if chemicals is None:
            chemicals = self.harmfulChemicals
            
        query = """
        SELECT A.AID, A.Name, A.startDate, A.endDate, 
               (SELECT COUNT(*) 
                FROM TaskChemicals TC 
                WHERE TC.AID = A.AID 
                  AND TC.Chemicals IN ({})
               ) AS Harmful_chemicals_count
        FROM Activity A
        JOIN HoldIn H ON A.AID = H.AID
        WHERE H.LocationName = ?
          AND A.startDate <= ?
          AND A.endDate >= ?
        GROUP BY A.AID, A.Name, A.startDate, A.endDate
        """.format(','.join(['?' for _ in chemicals]))
        
        params = chemicals + [location, startDate, endDate]
        return self.fetch_all(query, params)

    def getHarmfulChemicals(self):
        """Get all harmful chemicals"""
        return self.harmfulChemicals

    def addHarmfulChemical(self, chemical):
        """Add a harmful chemical"""
        if chemical not in self.harmfulChemicals:
            self.harmfulChemicals.append(chemical)
            return True
        return False

    def removeHarmfulChemical(self, chemical):
        """Remove a harmful chemical"""
        if chemical in self.harmfulChemicals:
            self.harmfulChemicals.remove(chemical)
            return True
        return False

    def getLocations(self):
        """Get all locations"""
        return self.fetch_all("SELECT Name FROM Location")

    def getWorkerDistribution(self):
        """Get worker distribution report data"""
        query = """
        SELECT W.WID, W.Name, COUNT(A.AID) as TaskCount, W.salary
        FROM Worker W 
        LEFT JOIN Assigned A ON W.WID = A.WID 
        GROUP BY W.WID, W.Name
        """
        return self.fetch_all(query)

    def getManagerWorkload(self):
        """Get manager workload report data"""
        query = """
        SELECT M.MID, M.Name, COUNT(DISTINCT L.Name) as SupervisedLocations, COUNT(DISTINCT W.WID) as SupervisedWorkers, M.salary
        FROM Manager M 
        LEFT JOIN Location L ON M.MID = L.Supervisor
        LEFT JOIN Worker W ON W.Supervisor = M.MID
        GROUP BY M.MID, M.Name
        """
        return self.fetch_all(query)

    def getOutsourceSummary(self):
        """Get outsource summary report data"""
        query = """
        SELECT C.CompanyID, C.Name, COUNT(W.AID) as ContractCount, SUM(W.ContractedPayment) as TotalPayment
        FROM Company C 
        LEFT JOIN WorkOn W ON C.CompanyID = W.CompanyID
        GROUP BY C.CompanyID, C.Name
        """
        return self.fetch_all(query)

    def getTableSchema(self, table_name):
        """Get table schema information"""
        query = f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        return self.fetch_all(query)

    def close(self):
        """Close database connection"""
        self.con.close()