import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="My_Hospital"
)

cur=myDB.cursor()
myTable = "CREATE TABLE Patients(Patient_ID INT PRIMARY KEY NOT NULL, Patient_Name VARCHAR(50) NOT NULL, Patient_Disease VARCHAR(50) NOT NULL)"
cur.execute(myTable)
print("Table Has Been Created")

