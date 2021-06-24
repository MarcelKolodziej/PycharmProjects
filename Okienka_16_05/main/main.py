import mysql.connector
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

root = Tk()
class Mainwindow:
    def __init__(self, root):
        self.root=root
        self.root.title("System Logowania")
        self.root.geometry("1200x700+200+70")
        self.root.resizable(False, False) # brak skalowania okienka


### ADDING IMAGE TO MAIN WINDOW ###

        self.image=ImageTk.PhotoImage(file="img1.jpg")
        self.label=Label(self.root, image=self.image) # Dodawanie obrazka
        self.label.pack()


### CREATE FRAME ON ROOT WINDOW ###

        self.frame = Frame(self.root)
        self.frame.place(x=390, y=170, width=400, height=450)

### CREATING LABELS AND ENTRY BOX ON FRAME ###
        self.userLabel = Label(self.frame, text="USER_ID", font=("Andalus", 15, 'bold'))
        self.userLabel.place(x=88, y=50)

        self.entry1=Entry(self.frame, font=("times new roman",15))
        self.entry1.place(x=88, y=100, width=250)

        self.passlabel=Label(self.frame,text="Password", font=('Andalus', 15, 'bold'),bg='white',fg='grey' )
        self.passlabel.place(x=80, y=150)

        self.entry2=Entry(self.frame, font=("times new roman", 15))
        self.entry2.place(x=88, y=200, width=250)

        self.button = Button(self.frame, text='Login', activebackground="#00B0F0", activeforeground='white', fg='black',
                             bg="#00B0F0", font=('Arial', 15, 'bold'),command=self.logindata)
        self.button.place(x=88, y=250, width=250)

###CREATING DATABASE CONNECTION ######
    def logindata(self):
        log=str(self.entry1.get())
        pas=str(self.entry2.get())
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user=log,
                password=pas,
                database="student_management"
            )
            self.succes = Label(self.root, text="Połączono", bg='green', font=('Andalus', 15, 'bold'))
            self.succes.place(x=475, y=500, width=250, )
        except:
            self.error = Label(self.root, text="Błąd połączenia", bg='red', font=('Andalus', 15, 'bold'))
            self.error.place(x=475, y=500, width=250,)


main = Mainwindow(root)     #wywołanie funkcji
root.mainloop()