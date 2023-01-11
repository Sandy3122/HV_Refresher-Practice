import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="herovired"
)

cur=myDB.cursor()
myData = "INSERT INTO Students(student_id, student_name, student_marks) VALUES(%s,%s,%s)"
vals = (101, 'Seeram', 95)
cur.execute(myData, vals)
myDB.commit()