import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sklep"
)

file = open('C:/Python/porshe.txt', 'r')
mycursor = mydb.cursor()

for file_content in file:
    x = file_content.split(" ")
    print(file_content)
    sql = "INSERT INTO samochody(id, marka, model, rocznik, kolor, stan) VALUES(%s,%s,%s,%s,%s,%s)"
    val = (x[0],x[1],x[2],x[3],x[4],x[5])
    mycursor.execute(sql, val)
    mydb.commit()

mydb.close()