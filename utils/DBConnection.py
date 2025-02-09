import sqlite3
import os

print("../DB/mydatabase.db:","Current directory:", os.getcwd())
print("**********************")


conn = sqlite3.connect('DB/mydatabase.db', check_same_thread=False)
print(f"Connected to database: {conn.execute('PRAGMA database_list').fetchall()}")
cursor = conn.cursor()


