from tkinter import *
window = Tk()

def function_clicKForName():
    imie = pole_tekstowe.get()
    etykieta_z_imieniem = Label(window, text=imie)
    etykieta_z_imieniem.grid(row=3, column=0)

def pobierz_liczbe():
    try:
        a = int(liczba.get())
        a = a + 10
        etykieta_z_liczba = Label(window, text=a)
        etykieta_z_liczba.grid(row=6, column=0)
    except:
        etykieta_z_liczba = Label(window, text="nie podales liczby")
    etykieta_z_liczba.grid(row=6, column=0)


window.title("Mój pierwszy program okienkowy")
window.geometry('400x300')
etykieta = Label(window, text="przykladowy tekst w etykiecie")
etykieta.grid(row=8,column=0)

etykieta2 = Label(window, text="Podaj swoje imie")
etykieta2.grid(row=1,column=1)

etykieta3 = Label(window, text="trzecia")
etykieta.place(x=150, y=200)

pole_tekstowe = Entry(width=33)
pole_tekstowe.grid(row=1,column=0)
przycisk = Button(window, text="kliknij mnie", width=20, command = function_clicKForName)
przycisk.grid(row=2, column=0)

##liczba
liczba = Entry(width=22)
liczba.grid(row=4, column=0)
przycisk_do_liczby = Button(window, text="kliknij mnie", width=20, command = pobierz_liczbe)
przycisk_do_liczby.grid(row=5, column=0)

#main Loop
window.mainloop()