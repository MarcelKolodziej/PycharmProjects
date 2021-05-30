# Create a connection files
# for the first time, create a table or format data scruture
# create cursor to execute SQL commands
# commit any changes, or confirm
# close the connection
import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS book (date text, trans text, symbol text, qty real, price real)''')
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
    cur.execute('''INSERT INTO book VALUES (NULL,?,?,?,?),(title, author, year, price ''')
    conn.commit()
    conn.close()

connect()
print(view())