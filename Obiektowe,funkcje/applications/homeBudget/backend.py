#TODO:
#autoinkrementacja primary key

# Create a connection files
# for the first time, create a table or format data scruture
# create cursor to execute SQL commands
# commit any changes, or confirm
# close the connection
import sqlite3
import time

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INT PRIMARY KEY, title TEXT, author TEXT, year INT, price INT )")
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute('''SELECT * FROM book''')
    rows = cur.fetchall()
    conn.close()
    return rows

def insert(title, author, year, price):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (1,?,?,?,?)",(title, author, year, price))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE title = 'Python'")
    conn.commit()
    conn.close()

connect()
print(view())
time.sleep(2)
# insert("Python", "Uruk-Hai", 2003, 20)
# print(view())
delete(1)
