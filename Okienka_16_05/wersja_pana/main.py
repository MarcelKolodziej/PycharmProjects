import mysql.connector
from tkinter import *
import menu

window = Tk()
window.title("logowanie do bazy")
window.geometry('400x300')
def logowanie():
    log=str(login.get())
    has=str(haslo.get())
    try:
        print(log)
        mydb = mysql.connector.connect(
            host="localhost",
            user=log,
            password=has,
            database="python"
        )
        menu.menu_lista()
    except:
        etykieta = Label(window, text="błąd połączenia")
        etykieta.grid(row=4, column=0)

login= Entry(window)
login.grid(row=1,column=0)
haslo= Entry(window)
haslo.grid(row=2,column=0)
przycisk = Button(window, text="kliknij mnie", width=20, command= logowanie)
przycisk.grid(row=3,column=0)

window.mainloop()