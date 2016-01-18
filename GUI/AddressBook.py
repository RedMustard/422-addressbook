"""
author: austin gheen
CIS422 Winter 2016

AddressBook.py
"""
import Tkinter as Tk

#def new_address_book() 

root = Tk.Tk()
root.title("Address Book")
#root.resizeable(10,10)

address_book_name = Tk.Entry(root)
address_book_name.grid(row=2, column = 1, pady = 10)
address_book_name.insert(0, 'Enter name')

#sumbit button to make a Address book names after the name entered
submit = Tk.Button(root, text='Submit')#, command = new_address_book ) #NEED TO MAKE BUTTON FUNCTIONAL
submit.grid(row = 3, column = 1)

#scroll bar for listbox of address books
scrollbar = Tk.Scrollbar(root)
scrollbar.grid(row = 4, column = 2)

#list of all the address books
book_list = Tk.Listbox(root, yscrollcommand = scrollbar.set)
book_list.grid(row = 4, column = 1, padx = 10, pady = 10)

scrollbar.config(command = book_list.yview)

if __name__ == "__main__":
	root.mainloop()