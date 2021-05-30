import tkinter as tk
from tkinter import *

def app_exit():
    exit()

def TotalBalans(self, totalbalans):
    self.totalbalans = totalbalans
    return 1

HEIGHT = 300
WIDTH = 400

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#263D42")
canvas.grid()

frame = tk.Frame(root, bg="white")

dodaj_wydatek = tk.Button(root, text="DODAJ WYDATEK")
dodaj_wydatek.grid(row=1, column=0)

dodaj_przychod = tk.Button(root, text="DODAJ PRZYCHOD")
dodaj_przychod.grid(row=2, column=0)

Balans = tk.Label(root, padx=2, pady=2, text="BALANS")
Balans.grid(row=0, column=0)

exitButton = tk.Button(root, text="Quit", padx=10, pady=5, fg="white", bg='#263D42', command=app_exit)
exitButton.grid(row=5, column=0)



#loop
root.mainloop()