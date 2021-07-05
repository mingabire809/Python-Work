import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",user="root",passwd="Michael60647", database = "pythons"
)

my_cursor = mydb.cursor()
update = "UPDATE employee SET sal=1000000 WHERE name='me'"
my_cursor.execute(update)

mydb.commit()