from tkinter import *

main_win = Tk()
main_win.title("Bookstore menager")

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
#loop
main_win.mainloop()