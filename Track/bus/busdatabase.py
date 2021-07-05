import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",user="root",passwd="Michael60647", database = "Bus"
)

my_cursor = mydb.cursor()
#my_cursor.execute("CREATE TABLE reservation(reference INT, name VARCHAR(200), destination VARCHAR(200), date DATETIME DEFAULT CURRENT_TIMESTAMP)")
#my_cursor.execute("ALTER TABLE reservation ADD COLUMN reference INT AFTER name;")
#my_cursor.execute('ALTER TABLE reservation ADD COLUMN bookingdate DATETIME DEFAULT CURRENT_TIMESTAMP;')
#my_cursor.execute('ALTER TABLE reservation Modify date varchar(20);')
#my_cursor.execute("CREATE TABLE Nairobi(reference INT, name VARCHAR(200), date varchar(20), bookingdate DATETIME DEFAULT CURRENT_TIMESTAMP)")
#my_cursor.execute("CREATE TABLE Bujumbura(reference INT, name VARCHAR(200), date varchar(20), bookingdate DATETIME DEFAULT CURRENT_TIMESTAMP)")
#my_cursor.execute("CREATE TABLE Mombasa(reference INT, name VARCHAR(200), date varchar(20), bookingdate DATETIME DEFAULT CURRENT_TIMESTAMP)")
#my_cursor.execute("CREATE TABLE Kigali(reference INT, name VARCHAR(200), date varchar(20), bookingdate DATETIME DEFAULT CURRENT_TIMESTAMP)")
my_cursor.execute("CREATE TABLE Kampala(reference INT, name VARCHAR(200), date varchar(20), bookingdate DATETIME DEFAULT CURRENT_TIMESTAMP)")
#my_cursor.execute("CREATE TABLE Juba(reference INT, name VARCHAR(200), date varchar(20), bookingdate DATETIME DEFAULT CURRENT_TIMESTAMP)")
#my_cursor.execute("CREATE TABLE Dar_es_Salam(reference INT, name VARCHAR(200), date varchar(20), bookingdate DATETIME DEFAULT CURRENT_TIMESTAMP)")
#my_cursor.execute('ALTER TABLE reservation ADD COLUMN bookingdate DATETIME DEFAULT CURRENT_TIMESTAMP;')