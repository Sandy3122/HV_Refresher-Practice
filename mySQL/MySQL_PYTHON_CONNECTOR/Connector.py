import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandeep@3122"
)
# print(myDB.connection_id)

'''
A cursor in database is a construct which allows you 
to iterate/traversal the records of a table.
'''
cur =myDB.cursor()
cur.execute("CREATE DATABASE HeroVired")    #HeroVired Is Database Name

# try:
#     print("Database Is Created")
# finally:
#     print("Not Created")