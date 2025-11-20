import sqlite3

def execute(command: str):
    return c.execute(command)

def update(table:str,change:dict,condition:str):
    changeToString=",".join([f"{k}={v}" for k,v in change.items()])
    c.execute(f"UPDATE {table} SET {changeToString}=? WHERE {condition};")

def view(table:str,condition:str=""):
    return execute(f"SELECT * FROM {table} WHERE {condition};")

def getTables():
    return [""]

conn = sqlite3.connect('data.db')
c = conn.cursor()