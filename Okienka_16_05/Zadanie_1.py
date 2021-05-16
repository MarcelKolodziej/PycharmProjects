from tkinter import *

window = Tk()

def window1():
    window.title("okienko pierwsze")
    window.geometry("200x200")
    button1 = Button(window, text="Uruchom okienko 2", command=window2)
    button1.grid(row=0, column=0)

    a = zmienna.get()
    etykieta = Label(window, text=a)
    etykieta.grid(row=3, column=0)

def window2():
    window.title("okienko drugie")
    window.geometry("300x300")
    button2 = Button(window, text="uruchom okienko 1", command=window1)
    button2.grid(row=0, column=0)

zmienna = IntVar()
r = Radiobutton(window, text = "wybór 1", variable=zmienna, value=1)
r.grid(row=0,column=0)
r = Radiobutton(window, text = "wybór 2", variable=zmienna, value=2)
r.grid(row=1,column=0)
przycisk = Button(window,text="Zatwierdz wybór",command=window1)
przycisk.grid(row=2,column=0)

window1()

window.mainloop()