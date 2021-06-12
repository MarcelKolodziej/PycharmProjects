import mysql.connector
from tkinter import *
def menu_lista():
    window = Tk()
    window.title("menu")
    window.geometry('400x300')
    etykieta = Label(window, text="tu jest menu")
    etykieta.grid(row=1, column=0)


    window.mainloop()