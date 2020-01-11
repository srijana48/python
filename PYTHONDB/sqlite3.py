import sqlite3
conn=sqlite3.connect('test.bd')
print ("opened successfully")
command="create table toto (id int,task text, date text,status text)"
conn.execute(command)
print("table created")