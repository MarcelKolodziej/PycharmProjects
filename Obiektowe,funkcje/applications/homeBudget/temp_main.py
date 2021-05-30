import db
from tkinter import *
from tkinter.ttk import *

LARGE_FONT = ("Verdana", 32)

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()

    #grid, labels, buttons windows will come shortly after


# the main function will be at the end of the script
def main():
    #db.create_tables(connection)
    root = Tk()
    root.geometry('250x200')
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)

    root.mainloop()


main()