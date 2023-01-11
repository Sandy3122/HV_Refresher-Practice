import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="herovired"
)

cur=myDB.cursor()
myData = "INSERT INTO Students(student_id, student_name, student_marks) VALUES(102,'Sandeep',100),(103,'Lakshman',95),(104,'Kumar',90)"
cur.execute(myData)
myDB.commit()