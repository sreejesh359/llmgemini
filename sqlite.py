import sqlite3
connection=sqlite3.connect("student.db")
cursor=connection.cursor()


cursor.execute("Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),ROLLNO VARCHAR(25))")


#INSRET INTO TABLE

cursor.execute('''insert into STUDENT values('sreeju','cs','301')''')
cursor.execute('''insert into STUDENT values('sreerag','cl','302')''')
cursor.execute('''insert into STUDENT values('abhi','ec','303')''')
cursor.execute('''insert into STUDENT values('bala','bt','304')''')


#display
data=cursor.execute("SELECT NAME FROM STUDENT WHERE ROLLNO=303;")
for row in data:
    print(" ".join(row))

connection.commit()
connection.close()