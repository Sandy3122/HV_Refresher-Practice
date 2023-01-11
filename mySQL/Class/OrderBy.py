import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="herovired"
)

cur=myDB.cursor()
cur.execute("SELECT * FROM Students ORDER BY Student_marks")
res = cur.fetchall()
for i in res:
    print(i)