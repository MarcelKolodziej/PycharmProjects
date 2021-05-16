import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Ankieta")
root.geometry("300x300")
heading = Label(text="Ankieta",fg="black",bg="yellow",width="30",height="3",font="4")
heading.grid(row=0, column=0)
root.geometry("400x500")

# Functions
def saveData():
    myLabel3 = Label(root, text="Zapisano!")
    myLabel3.grid(row=10, column=0)

    first_name_info = name_var.get()
    second_name_var = second_name.get()
    print(first_name_info)
    print(second_name_var)
    print(plec_M)

    file = open("user.txt", "w")
    file.write("Twoje imie " + first_name_info)
    file.write("\n")
    file.write("Twoje nazwisko " + second_name_var)
    file.write("\n")

# Creating Label

name_var = StringVar()
second_name_var = StringVar()
plec_M = StringVar(root, "M")
# plec_K = StringVar(app, "K")
# age = IntVar()

####### Shoving into screen
name_label = Label(text="First name:")
name_label.grid(row=1, column=0)
name = Entry(root,textvariable=name_var, width=30)
name.grid(row=2, column=0, padx=10, pady=10)

second_name_label = Label(text="Second name:")
second_name_label.grid(row=3, column=0)
second_name = Entry(root, textvariable=second_name_var, width=30)
second_name.grid(row=4, column=0, padx=10, pady=10)

age_label = Label(text="Age: ")
age_label.grid(row=5, column=0)
age = Entry(root, width=30)
age.grid(row=6, column=0, padx=10, pady=10)

gender_label = Label(text="Choose Gender")
gender_label.grid(row=7, column=0, padx="30")
gender_M_button = Radiobutton(root, text="M", variable="", value=1)
gender_M_button.grid(row=8, column=0)

gender_K_button = Radiobutton(root, text="K", variable="", value=2)
gender_K_button.grid(row=9, column=0)

gender_label = Label(text="Choose Your Grades")
gender_label.grid(row=10, column=0, padx="30")

# Buttons
myButton = Button(root, text="Zapisz Dane!",command=saveData)
myButton.grid(row=15, column=0)

root.mainloop()