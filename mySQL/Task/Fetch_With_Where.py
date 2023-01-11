import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="my_Hospital"
)

cur=myDB.cursor()
cur.execute("SELECT * FROM Patients WHERE Patient_Disease = 'Covid'")
res = cur.fetchall()
for i in res:
  print(i)