# Importy
from tkinter import *

# Init
app = Tk()
ma = IntVar(None)
he = IntVar(None)
b = IntVar(None)


# Obliczanie BMI z podanych liczb, sprawdzenie kategori wagowej
# Sprawdzenie, czy podana liczba nie jest zerem

def calculate_bmi():
    try:
        bmi = float(mass.get()) / (float(height.get()) * float(height.get()))
        b.set(bmi)
    except ZeroDivisionError:
        ma.set(None)
        he.set(None)
        b.set(None)
        return
    if bmi < 18.5:
        resLabelText.set("Masz niedowagę!")
    if 18.5 < bmi < 24.9:
        resLabelText.set("Wszystko w porządku :)")
    if 25 < bmi < 29.9:
        resLabelText.set("Masz lekką nadwagę...")
    if bmi > 30:
        resLabelText.set("Koniecznie zaprzestań jedzenia!")
    return

########################### GUI ###########################################

#  Sets size and title
app.geometry("350x200+100+100")
app.title("BMI Calculator")

# Label and test box for mass in kg
mLabelText = StringVar()
mLabelText.set("Podaj wagę w kilogramach: ")
massLabel = Label(app, textvariable=mLabelText)
massLabel.pack()

mass = Entry(app, textvariable=ma)
mass.pack()

# Label and text box for height
hLabelText = StringVar()
hLabelText.set("Podaj wzrost: ")
heightLabel = Label(app, textvariable=hLabelText)
heightLabel.pack()

height = Entry(app, textvariable=he)
height.pack()

# Button and label and textbox for BMI calculation
button = Button(app, text="Calculate BMI", command=calculate_bmi)
button.pack(padx=15, pady=15)
bmiLabelText = StringVar()
bmiLabelText.set("Twoje BMI: ")
bmiLabel = Label(app, textvariable=bmiLabelText)
bmiLabel.pack()

bmi = Entry(app, textvariable=b)
bmi.pack()
resLabelText = StringVar()
resLabelText.set(" twoja kategoria wagowa: ")
resLabel = Label(app, textvariable=resLabelText)
resLabel.pack()

# Starts the GUI
app.mainloop()