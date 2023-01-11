import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="my_Hospital"
)

cur=myDB.cursor()
myData = "INSERT INTO Patients(Patient_ID, Patient_Name, Patient_Disease) VALUES(%s,%s,%s)"
vals = [
    (101, 'Unknown1', "Covid"),
    (102, 'Unknown2', "Malaria"),
    (103, 'Unknown3', "Diarrhea"),
    (104, 'Unknown4', "Diarrhea"),
    (105, 'Unknown5', "Covid"),
    (106, 'Unknown6', "Malaria"),
    (107, 'Unknown7', "Covid"),
    (108, 'Unknown8', "None")
]
cur.executemany(myData, vals)
myDB.commit()
print("Data Has Been Inserted Successfully")