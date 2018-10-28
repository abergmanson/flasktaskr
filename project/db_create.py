# /project/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")

    #insert dummy data
    c.execute('INSERT INTO tasks(name, due_date, priority, status)'
              'VALUES("Finish this tutorial", "10/29/2018", 10, 1)')

    c.execute('INSERT INTO tasks(name, due_date, priority, status)'
              'VALUES("Finish RealPython Part 2", "01/01/2019", 10, 1)')

