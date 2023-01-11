import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="herovired"
)

cur=myDB.cursor()
myData = "INSERT INTO Students(student_id, student_name, student_marks) VALUES(%s,%s,%s)"
vals = [
    (105, 'Sandy', 85),
    (106, 'Sona', 80)
]
cur.executemany(myData, vals)
myDB.commit()