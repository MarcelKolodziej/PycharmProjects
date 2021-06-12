#TODO:
#naprawić usuwanie

# Create a connection files
# for the first time, create a table or format data scruture
# create cursor to execute SQL commands
# commit any changes, or confirm
# close the connection
import sqlite3
import time
import os
from pprint import pprint


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER primary key AUTOINCREMENT, title TEXT, author TEXT, year INT, price INT )")
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
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, price))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE title = 'Python1'")
    conn.commit()
    conn.close()

def search(title = "", author = "", year = "", price = ""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR price = ?",(title,author,year,price))
    rows = cur.fetchall()
    conn.close()
    return rows

def update(id,title,author,year,price):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, price = ? WHERE id = ?",(title,author,year,price,id))    #kolejnosc ma znaczenie
    conn.commit()
    conn.close()

connect()
os.system("cls")

# update(1, "book1", "author1", 2000, 500,)

# time.sleep(2)
# insert("Python4", "Uruk-Hai", 2003, 20)
# pprint(view())
# delete(None)
