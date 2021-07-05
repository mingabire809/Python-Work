import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",user="root",passwd="Michael60647",
)

my_cursor = mydb.cursor()
my_cursor.execute(" CREATE DATABASE Pythons ")

my_cursor.execute('SHOW DATABASES')
for db in my_cursor:print(db)
if(mydb):
    print("Successful")
else:
    print("unsuccessful")