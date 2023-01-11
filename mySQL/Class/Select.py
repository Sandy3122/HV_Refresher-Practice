import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122",
    database="herovired"
)

cur=myDB.cursor()
cur.execute("SELECT * FROM Students")
res = cur.fetchall()
# print(res)
for i in res:
  print(i)


# fetchall()
# res =  cur.fetchall()
# print(res)    #The Result Will Be Array Format

#To Fetch Only One Data
# res = cur.fetchone()
# print(res)


# fetchmany()
# res = cur.fetchmany(2) #we have to mention number of rows to be printed
# print(res)