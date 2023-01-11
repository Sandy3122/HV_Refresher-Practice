import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="herovired"
)

cur=myDB.cursor()
cur.execute("SELECT * FROM Students WHERE student_id = 104")

# res = cur.fetchall()
# for i in res:
#   print(i)

#If we know the data will be only one
print(cur.fetchone())