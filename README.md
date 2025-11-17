2025/11/12 Ruiyang
    I'm focusing on the GUI section of this project. I wish that the execution part could satisify the following function:
    1. a function for executing a sql commad and return the result: execute(command: str) --> list;
    2. a function that returns the content of a table by name getTableContent(tableName: str) --> list;

2025/11/12 Ziru

  I have uploaded the SQL script that is used to set up the database to database/configuration.sql 
  
  Kindly note that:  
  1. I have NOT set up indecies but attached the proposed script at the end of the file. I am not sure about these script, and they need to be discussed before being put into the dbms.  
  2. All date input MUST follow ISO-8601 format in order to facilitate comparision between dates and avoid ambiguity.  
        To be specific, the format is **YYYYMMDD + T + HHMMSS + Time Zone**  
        - For example, HKT 23:41:00, 12 November, 2025 should be represented as **20251112T234100+08**.  
        You can also store a date without a specific time. The format would be much simplier: **YYYYMMDD**.  
        - For example, 12 Nov 2025 should be represented as **20251112**.  
  3. I will not upload the database file because git can only handle text files and attempting to upload binary files like a database might mess up the whole repo.  
        - It is recommended that we upload the db entries in text forms (or better, in SQL commands).  
        - You can set up your own db using the script (database/configuration.sql) with SQLite. (https://sqlite.org/download.html)  
        - To run the script, type "./sqlite3.exe campus.db < configuration.db" in your terminal. Make sure that configuration.db is in your current directory.

2025/11/17 Ruiyang
      1. Update GUI, completed the first tab. 
      2. Updated GUI, completed the first and second tab.

