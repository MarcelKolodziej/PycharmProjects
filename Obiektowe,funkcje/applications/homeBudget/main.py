from tkinter import *

#Tkinter settings
main_win = Tk()
main_win.title("Bookstore menager")

# Logic
def view_command():
    pass

def search_command():
    pass

def add_command():
    pass

def update_command():
    pass

def delate_command():
    pass

def delate_command():
    pass

def exit_command():
    exit()


l_title =  Label(main_win, text = "Title" )
l_title.grid(row=0, column=0)
title_text = StringVar()
e_title = Entry(main_win, textvariable=title_text)
e_title.grid(row=0, column=1)

l_author = Label(main_win, text = "Author")
l_author.grid(row=0, column=2)
author_text = StringVar()
e_author = Entry(main_win, textvariable=author_text)
e_author.grid(row=0, column=3)

l_year = Label(main_win, text = "Year")
l_year.grid(row=1, column=0)
year_text = StringVar()
e_year = Entry(main_win, textvariable = year_text)
e_year.grid(row=1, column=1)

l_price = Label(main_win, text = "Price")
l_price.grid(row=1, column=2)
price_text = StringVar()
e_price = Entry(main_win, textvariable=price_text)
e_price.grid(row=1, column=3)

list_box = Listbox(main_win, height= 8, width = 30)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

# buttons
b_view = Button(main_win, text = "View all", width=10, command = view_command)
b_view.grid(row=3, column=3)

b_search = Button(main_win, text = "Search", width=10, command = search_command)
b_search.grid(row=2, column=3)

b_add = Button(main_win, text = "Add", width=10, command = add_command)
b_add.grid(row=4, column=3)

b_update = Button(main_win, text = "Update", width=10, command = update_command)
b_update.grid(row=5, column=3)

b_delate = Button(main_win, text = "Delate", width=10, command = delate_command)
b_delate.grid(row=6, column=3)

b_exit = Button(main_win, text = "Exit", width = 10, command = exit_command)
b_exit.grid(row=7, column=3)

#loop
main_win.mainloop()