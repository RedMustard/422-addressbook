"""
author: austin gheen
CIS422 Winter 2016

main address book window.
	-lists all contact entries and has a scroll bar
	-buttons:
		create new address book 
		save currently opened address book 
		open previouslly viewed address book
		edit contact selection from the listbox (book_list)
	-message widget to view contact info. (Might need to change)

"""
import Tkinter as Tk

#commented out the commands and methods for the buttons to be able to run the file with broken buttons

#add a new addbook
#def new_addbook():


#open previouslly viewed book
#def open_prevbook():


#saves address book
#def save_addbook():

#edit selected contact
#def edit_contact():


root = Tk.Tk()
root.title("Address Book")

#button to make new addbook
new_button = Tk.Button(root, text='New')#, command = new_addbook ) #NEED TO MAKE BUTTON FUNCTIONAL
new_button.grid(row = 1)

#button to open previouslly viewed addbook
open_button = Tk.Button(root, text='Open')#, command = open_prevbook ) #NEED TO MAKE BUTTON FUNCTIONAL
open_button.grid(row = 2)

#button to save current addbook
save_button = Tk.Button(root, text='Save')#, command = save_addbook) #NEED TO MAKE BUTTON FUNCTIONAL
save_button.grid(row = 3)

scrollbar = Tk.Scrollbar(root)
scrollbar.grid(row = 4, column = 1)

#list of all the address book's contacts
book_list = Tk.Listbox(root, yscrollcommand = scrollbar.set)
book_list.grid(row = 4, pady = 10)
#some example inputs
for i in range(10):
	book_list.insert(0 ,str(i))

scrollbar.config(command = book_list.yview)

#example text
contact_info = Tk.Message(root, text = "CONTACT INFO WILL BE DISPLAYED HERE")
contact_info.grid(row = 4, column = 2)

#button to edit selected contact
edit_button = Tk.Button(root, text = 'Edit')#, command = edit_contact ) #NEED TO MAKE BUTTON FUNCTIONAL
edit_button.grid(row = 5, column = 2)

if __name__ == "__main__":
	root.mainloop()