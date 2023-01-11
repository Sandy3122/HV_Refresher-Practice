import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="herovired"
)

cur=myDB.cursor()
# cur.execute("DELETE FROM Students WHERE student_id = 106")
# myDB.commit()       #commiting to the database
# print("Data Has Been Deleted")




rows = cur.execute('select * from students')
res = cur.fetchall()
for x in res:
    if('SELECT student_id FROM Students WHERE student_id = 103') == "Lakshman":
        cur.execute("DELETE FROM Students WHERE student_id = 103")
        myDB.commit()
        print("Data Has Been Deleted")
    else:
        print("Data Not Present")
