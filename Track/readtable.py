import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",user="root",passwd="Michael60647", database = "pythons"
)

my_cursor = mydb.cursor()
my_cursor.execute("Select * from employee")
result = my_cursor.fetchall()
for row in result:
    print(row)
