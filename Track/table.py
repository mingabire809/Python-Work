import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",user="root",passwd="Michael60647", database = "pythons"
)

my_cursor = mydb.cursor()
#my_cursor.execute("CREATE TABLE employee(name VARCHAR(200), sal INT(20))")
my_cursor.execute("Show tables")
for tb in my_cursor:
    print(tb)