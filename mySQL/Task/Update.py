import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="my_Hospital"
)

cur=myDB.cursor()
cur.execute("UPDATE Patients SET Patient_Name= 'Mister' WHERE Patient_Disease = 'None'")
myDB.commit()       #commiting to the database
print("Data Has Been Updated")