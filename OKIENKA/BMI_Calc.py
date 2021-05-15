import tkinter
from tkinter import *

root = Tk()
root.geometry("300x150")
root.title("BMI kalkulator")

# Funcions
def calculate_BMI():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2), 2)
    label_result['text'] = f"BMI: {bmi}"
    print(round(bmi, 2))

# GUI
label_kg = Label(root, text= "KG: ")
label_kg.pack()

entry_kg = tkinter.Entry(root)
entry_kg.pack()

label_height = Label(root, text= "HEIGHT: ")
label_height.pack()

entry_height = tkinter.Entry(root)
entry_height.pack()

label_result = Label(root, text= "BMI: ")
label_result.pack()

button_calculate = tkinter.Button(root, text="Calculate", command=calculate_BMI)
button_calculate.pack()
root.mainloop()