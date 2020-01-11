import sqlite3
conn=sqlite3.connect('employe.db')
print("open database successfully")
command="select *from company"
result=conn.execute(command)
r=result.fetchall()
print(r)



