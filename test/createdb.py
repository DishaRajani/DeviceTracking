import sqlite3
from ardRfid import run
from datetime import datetime


db = sqlite3.connect('data.db')
cursor = db.cursor()

query = "CREATE TABLE devices(device_id TEXT PRIMARY KEY, description TEXT)"
cursor.execute(query)

# query = "INSERT INTO devices VALUES(?, ?)"
#id1 = run()
# cursor.execute(query, (id1, "printer lab 1"))
# print('next')
#id2 = run()
# cursor.execute(query, (id2, "printer lab 2"))

query = "CREATE TABLE labs(lab_id INTEGER PRIMARY KEY, description TEXT)"
cursor.execute(query)

query = "INSERT INTO labs VALUES(?, ?)"
cursor.execute(query, (1, "1st floor lab"))
cursor.execute(query, (2, "2nd floor lab"))

query = "CREATE TABLE belongs(lab_id INTEGER, device_id TEXT, status TEXT, current_lab INTEGER)"
cursor.execute(query)

# query = "INSERT INTO belongs VALUES (?, ?, ?, ?)"
# cursor.execute(query, (1, id1, "in", 1))
# cursor.execute(query, (2, id2, "in", 2))

query = "CREATE TABLE log(device_id TEXT, current_lab_id INTEGER, status TEXT, time timestamp)"
cursor.execute(query)

# query = "INSERT INTO log VALUES (?, ?, ?, ?)"
# cursor.execute(query, (id1, 1, "in", datetime.now()))
# cursor.execute(query, (id2, 2, "in", datetime.now()))

query = "CREATE TABLE IF NOT EXISTS login(ID INTEGER PRIMARY KEY AUTOINCREMENT, staff_name VARCHAR, staff_email VARCHAR, username VARCHAR, password VARCHAR)"
cursor.execute(query)
query = "INSERT INTO login(username,password) VALUES('admin','admin')"
cursor.execute(query)

db.commit()
