import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'sklep'
)

mycursor = mydb.cursor()

'''mycursor.execute("CREATE TABLE example (id INT AUTO_INCREMENT PRIMARU ")'''

for x in mycursor:
  print(x)



