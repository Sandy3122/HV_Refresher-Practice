import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="my_Hospital"
)

cur=myDB.cursor()
cur.execute("UPDATE Patients SET Patient_Name= 'Unknow_Guy', Patient_Disease='Malaria' WHERE Patient_ID=105")
myDB.commit()       #commiting to the database
print("Data Has Been Updated")