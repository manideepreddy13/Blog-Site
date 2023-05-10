import sqlite3

# connection with the database

conn = sqlite3.connect('database.db')

# open the sql file and execute the contents inside the file to create the posts table

with open('blogschema.sql') as f:
    conn.executescript(f.read())

# cursor object to execute further sql statements one by one

curr = conn.cursor()

curr.execute("INSERT INTO posts ('title','content') VALUES (?, ?)",('First Post','Content 1'))

curr.execute("INSERT INTO posts ('title','content') VALUES (?, ?)",('Second Post','Content 2'))

conn.commit()

conn.close()
