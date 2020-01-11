import sqlite3
conn=sqlite3.connect('test.db')
command="create table todo(id int,task text,date text,status text)"
comand="insert into todo(id,task,date,status)
values(1,'study machine language','26-11-2019','complete')"
command="insert into todo(id,task,date,status)
values(2,'exercies','dailly','done')"
conn.execute(command)
conn.commit()