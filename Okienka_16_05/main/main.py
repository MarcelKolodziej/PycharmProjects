from tkinter import messagebox
import pymysql
from tkinter import *
from PIL import ImageTk


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
                             bg="#00B0F0", font=('Arial', 15, 'bold'))
        self.button.place(x=88, y=250, width=250)

###CREATING DATABASE CONNECTION ######
    def Logindata(self):
        con=pymysql.connect("localhost", 'root', 'Sagar123', 'student_menager')
        cur = con.cursor()
        cur.execute("Select * from admin_data where User_ID=%s and Password=%s,"(self.entry1.get(), self.entry2.get()))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("WARNING","USER NOT FOUND")
        else:
            messagebox.showinfo("Succes","Login successfully")

main = Mainwindow(root)     #wywołanie funkcji
root.mainloop()