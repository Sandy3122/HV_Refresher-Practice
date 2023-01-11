import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="herovired"
)

cur=myDB.cursor()
cur.execute("UPDATE Students SET Student_marks= 100 WHERE student_id = 101")
myDB.commit()       #commiting to the database
print("Data Has Been Updated")




# #open cursor 
# cur1 = myDB.cursor() 
# cur2 = myDB.cursor()

# #Execute SQL to update 
# cur1.execute("UPDATE Students SET Student_marks=120 WHERE student_id = 101")
# aList = [item[0] for item in cur1.fetchall()] 
# for row in cur1.fetchall():
#         cur2.execute("UPDATE Students SET Student_marks=? WHERE student_id = ?",(120,101))
#         myDB.commit()
#         print("Data Has Been Updated")
# cur1.close() 
# cur2.close()

# rows = cursor.execute('select * from tabela1').fetchall()
# for acc_row in rows:
#     cursor.execute('UPDATE table_name SET column_name=? where column_name=?', (acc_row.column1, acc_row.column2))