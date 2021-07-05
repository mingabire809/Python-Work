import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",user="root",passwd="Michael60647", database = "pythons"
)

my_cursor = mydb.cursor()
form = "Insert into employee(name,sal) values(%s,%s)"
link = 'my link'
money = 22000
employees = [('Me',250000),('You',250000),('Him',250000),('Us',750000),('You',580000),('Them',745000),(link,money),]
my_cursor.executemany(form, employees)
mydb.commit()