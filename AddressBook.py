"""
author: austin gheen
CIS422 Winter 2016

AddressBook.py
"""
import tkinter as Tk
import main as m

def item_return():
	r = item.get()
	m.add_contact(r)
	book_list.insert(Tk.END, m.get_contacts('last'))
	# return r

root = Tk.Tk()
root.title("Address Book")
#root.resizeable(10,10)

item = Tk.Entry(root)
item.grid(row=2, column = 1, pady = 10)
item.insert(0, 'Enter name')


#sumbit button to make a Address book names after the name entered
submit = Tk.Button(root, text='Submit', command = item_return) #NEED TO MAKE BUTTON FUNCTIONAL
submit.grid(row = 3, column = 1)

#scroll bar for listbox of address books
scrollbar = Tk.Scrollbar(root)
scrollbar.grid(row = 4, column = 2)

#list of all the address books
book_list = Tk.Listbox(root, yscrollcommand = scrollbar.set)
book_list.grid(row = 4, column = 1, padx = 10, pady = 10, columnspan= 3)

scrollbar.config(command = book_list.yview)

if __name__ == "__main__":
	root.mainloop()