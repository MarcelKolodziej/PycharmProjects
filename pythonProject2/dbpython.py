import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sklep"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM samochody ")

myresult = mycursor.fetchall()

for linia in myresult:
    print(linia)
#write to file
f = open("C:/Python/pythondatabase.txt", "w")

for flinia in myresult:
    f.write(str(flinia))
f.close()

