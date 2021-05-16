from tkinter import *

window = Tk()
window.title('kalkulator BMI')
window.geometry('600x600')

def func():
    try:
        a = float(pole.get())
        b = float(pole1.get())
        result = round(a / (b * b), 2)
        pole_result = Label(window, width=22, text=result)
        pole_result.grid(row=3, column=5)
        if result < 18.5:
            pole_result1 = Label(window, width=22, text='niedowaga')
            pole_result1.grid(row=4, column=5)
        else:
            if ((result > 18.5)) & (result < 24.9):
                pole_result1 = Label(window, width=22, text='prawidlowa waga')
                pole_result1.grid(row=4, column=5)
            else:
                if ((result > 25.0)) & ((result < 29.9)):
                    pole_result1 = Label(window, width=22, text='nadwaga')
                    pole_result1.grid(row=4, column=5)
    except:
        pole_result = Label(window, text="nie podales liczby")

waga = Label(window, text='waga, w kg')
waga.grid(row=0, column=0)
pole = Entry(width=20)
pole.grid(row=1, column=0)
wzrost = Label(window, text='wzrost w m')
wzrost.grid(row=0, column=10)
pole1 = Entry(width=20)
pole1.grid(row=1, column=10)

przycisk = Button(window, text='Twoje BMI to', width=20, command=func)
przycisk.grid(row=2, column=5)
window.mainloop()