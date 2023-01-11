import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="herovired"
)

cur=myDB.cursor()
myTable = "CREATE TABLE Students(student_id INT PRIMARY KEY NOT NULL, student_name VARCHAR(50) NOT NULL, student_marks INT NOT NULL)"
cur.execute(myTable)
print("Table Has Been Created")

