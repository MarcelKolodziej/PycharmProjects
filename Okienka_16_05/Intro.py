from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Ankieta")
root.geometry("300x300")
root.geometry("400x500")

# Style class to add style to Radiobutton
# it can be used to style any ttk widget
style = Style(root)
style.configure("TRadiobutton", background = "light green",
                foreground = "red", font = ("arial", 10, "bold"))

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
v = StringVar()
##############################################
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}
#############################################

for (text, value) in values.items():
    Radiobutton(root, text = text, variable = v,
                value = value).pack(side = TOP, ipady = 5)

#############################################
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