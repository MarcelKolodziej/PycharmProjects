from tkinter import *
from PIL import ImageTk


root = Tk()
class Mainwindow:
    def __init__(self, root):
        self.root=root
        self.root.title("System Logowania")
        self.root.geometry("1200x700+200+70")
        self.root.resizable(False, False) # brak skalowania okienka


### Dodawanie obrazka na głównym okienku ###

        self.image=ImageTk.PhotoImage(file="img1.jpg")
        self.label=Label(self.root, image=self.image)
        self.label.pack()

main = Mainwindow(root)     #wywołanie funkcji
root.mainloop()