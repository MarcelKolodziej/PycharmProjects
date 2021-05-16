from tkinter import *

window = Tk()

def window1():
    window.title("okienko pierwsze")
    window.geometry("200x200")
    button1 = Button(window, text="Uruchom okienko 2", command=window2)
    button1.grid(row=0, column=0)

def window2():
    window.title("okienko drugie")
    window.geometry("300x300")
    button2 = Button(window, text="uruchom okienko 1", command=window1)
    button2.grid(row=0, column=0)

window1()

window.mainloop()