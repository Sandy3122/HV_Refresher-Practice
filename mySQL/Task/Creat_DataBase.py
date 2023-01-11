import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122"
)

cur =myDB.cursor()
cur.execute("CREATE DATABASE My_Hospital")
print("Database Has Been Created")