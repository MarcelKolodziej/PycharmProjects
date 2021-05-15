import tkinter
from tkinter import *

root = Tk()
root.geometry("300x150")
root.title("BMI kalkulator")


# Funcions
def calculate_BMI():
    try:
        kg = float(entry_kg.get())
        height = float(entry_height.get())
        bmi = round(kg / (height ** 2), 2)
        label_result['text'] = f"BMI: {bmi}"
        print(round(bmi, 2))
    except:
        label_results = Label(root, text="zle liczby")
    label_results.grid(column=2, row=1)



################ GUI #####################
label_kg = Label(root, text="KG: ")
label_kg.grid(column=0, row=0)

entry_kg = tkinter.Entry(root)
entry_kg.grid(column=1, row=0)

label_height = Label(root, text="HEIGHT: ")
label_height.grid(column=0, row=1)

entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row=1)

button_calculate = tkinter.Button(root, text="Calculate", command=calculate_BMI)
button_calculate.grid(column=0, row=2)

label_result = Label(root, text="BMI: ")
label_result.grid(column=1, row=2)
################ GUI #####################
root.mainloop()
