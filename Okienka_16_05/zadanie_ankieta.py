from tkinter import *

def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    plec_info = plec_M.get()

    print(firstname_info, lastname_info, plec_info, age_info)

    file = open("user.txt", "w")

    file.write("Twoje imie " + firstname_info)

    file.write("\n")

    file.write("Twoje nazwisko " + lastname_info)

    file.write("\n")

    file.write("Twoja plec " + plec_info)

    file.write("\n")

    file.write("Twój wiek " + str(age_info))

    file.close()


app = Tk()

app.geometry("400x500")

app.title("Ankieta")

heading = Label(text="Ankieta", fg="black", bg="lightblue", width="500", height="3", font="10")

heading.pack()

firstname_text = Label(text="Imie :")
lastname_text = Label(text="Nazwisko :")
plec_info = Label(text="Plec:")
age_text = Label(text="Wiek :")

# Dictionary to create multiple buttons
values = {" 1": "1",
          " 2": "2",
          " 3": "3",
          " 4": "4",
          " 5": "5"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(app, text=text, variable=plec_info,
                value=value).pack(side=TOP, ipady=5)

firstname_text.place(x=15, y=70)
lastname_text.place(x=15, y=140)
plec_info.place(x=15, y=210)
age_text.place(x=15, y=280)

firstname = StringVar()
lastname = StringVar()
plec_M = StringVar(app, "M")
plec_K = StringVar(app, "K")
age = IntVar()

first_name_entry = Entry(textvariable=firstname, width="30")
last_name_entry = Entry(textvariable=lastname, width="30")
plec_M_entry = Radiobutton(textvariable=plec_M, text = "wybór 2", value=2)
age_entry = Entry(textvariable=age, width="30")


first_name_entry.place(x=15, y=100)
last_name_entry.place(x=15, y=180)
plec_M_entry.place(x=25, y=240)
age_entry.place(x=15, y=300)

button = Button(app, text="Zapisz dane", command=save_info, width="30", height="2", bg="grey")

button.place(x=15, y=290)

mainloop()