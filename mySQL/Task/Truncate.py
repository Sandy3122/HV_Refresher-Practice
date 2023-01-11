import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="my_Hospital"
)

cur=myDB.cursor()
cur.execute("TRUNCATE TABLE Patients")
myDB.commit()       #commiting to the database
print("Table Data Has Been Deleted")