import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",user="root",passwd="Michael60647", database = "pythons"
)

my_cursor = mydb.cursor()
delete = "DELETE FROM employee WHERE name='me'"
my_cursor.execute(delete)
mydb.commit()