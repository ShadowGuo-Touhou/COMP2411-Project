2025/11/12 Ruiyang
    I'm focusing on the GUI section of this project. I wish that the execution part could satisify the following function:
    1. a function for executing a sql commad and return the result: execute(command: str) --> list;
    2. a function that returns the content of a table by name getTableContent(tableName: str) --> list;

2025/11/12 Ziru (Updated 20 Nov)  

  I have uploaded the SQL script that is used to set up the database to database/configuration.sql 
  
  Kindly note that:  
  1. I have NOT set up indecies but attached the proposed script at the end of the file. I am not sure about these script, and they need to be discussed before being put into the dbms.  
  2. All date input MUST follow ISO-8601 format in order to facilitate comparision between dates and avoid ambiguity.  
        To be specific, the format is **YYYY-MM-DD + T + HH:MM:SS**  
        - For example, HKT 23:41:00, 12 November, 2025 should be represented as **2025-11-12T23:41:00**.  
        You can also store a date without a specific time. The format would be much simplier: **YYYY-MM-DD**.  
        - For example, 12 Nov 2025 should be represented as **2025-11-12**.  
  3. Binary files, like a .db one, should be listed in _.gitignore_. Otherwise may destroy the whole repo. 
        - It is recommended that we upload the db entries in text forms (or better, in SQL commands).  
        - You can set up your own db using the script (database/configuration.sql) with SQLite. (https://sqlite.org/download.html)  
        - To run the script, type "./sqlite3.exe campus.db < configuration.db" in your terminal. Make sure that configuration.db is in your current directory.

2025/11/17 Ruiyang  
      1. Update GUI, completed the first tab.  
      2. Updated GUI, completed the first and second tab.  
      3. Updated GUI, completed the manage tab.  

2025/11/20 Jimmy  
      1. Sample code to create a db, use it or dump it.  
      2. the db name is setted through the config.py  
      3. vibe coded a test data generator, run 'python database/main.py' will create db with data innit  
      4. You are now required to have faker and pyqt6 to run the program  
      5. btw I fixed the get building thing in the gui  

2025/11/20 Ziru  
      **IMPORTANT**: Please be aware that the _format_ of date and time has been revised. (see above)  
      1. Date and Time format revised.  
      2. Attribute "Chemicals" in table "Task" **violates 1NF**. I created another table **TaskChemicals**. (see database/configuration.sql)  
