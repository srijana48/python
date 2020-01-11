import sqlite3
conn=sqlite3.connect('test.db')
command="select *from todo"
result=conn.execute(command)
for row in result:
    id,task,date,status=row
    print(id,task,date,status)

    
