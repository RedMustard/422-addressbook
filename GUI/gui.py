"""Address Book GUI

Authors: Austin Gheen, Travis Barnes
CIS422 Winter 2016

AddressBook.py
"""
import sys
sys.path.insert(0, '..')

import tkinter as Tk
import AddressBook as ab
import new # New address book window
import ecw # Edit Contact Window
import acw # Add Contact Window



#  Need a function that initializes a new database upon application opening. i.e. when you
# 		input the name of the database, a call is made to add any existing entries into book_list
#  Check out field_return to see how the call is made to get_contacts_list()

class mainWindow(object):

	def close_window(self):
		self.top.destroy()

	def contact_list(self):
		"""Retrieves list of contacts"""
		self.book_list.delete(0, Tk.END)
		for contact in ab.get_contacts_list('last'):
			self.book_list.insert(Tk.END, contact[0] + " " + contact[1])

	def field_return(self):
		i = 0
		r = self.item.get()
		ab.add_contact(r)
		self.book_list.delete(0, Tk.END)
		for contact in ab.get_contacts_list('last'):
			self.book_list.insert(Tk.END, contact[0]+contact[1])

	def popupNew_Addbook(self):
		self.n = new.New_AddBookWindow(self.master)
		self.master.wait_window(self.n.top)


	def popupAdd(self):
		self.w=acw.AddContactWindow(self.master)
		self.master.wait_window(self.w.top)

	def popupEdit(self):
		self.k=ecw.EditContactWindow(self.master)
		self.master.wait_window(self.k.top)


	def __init__(self,master):
		self.master = master
		master.title('Address Book')

		#entry field
		# self.item = Tk.Entry(master)
		# self.item.grid(row=0, column = 1, pady = 10)
		# self.item.insert(0, 'Enter name')

		#submit button
		# self.submit = Tk.Button(master, text='Submit', command = self.field_return)
		# self.submit.grid(row = 1, column = 1)

		#new address book button
		self.new_button = Tk.Button(master, text='New', command = self.popupNew_Addbook)
		self.new_button.grid(row = 1, column = 2)


		#scroll bar and box list of contacts
		self.scrollbar = Tk.Scrollbar(master)
		self.scrollbar.grid(row = 2, column = 2)
		self.book_list = Tk.Listbox(master, yscrollcommand = self.scrollbar.set)
		self.book_list.grid(row = 2, column = 1, padx = 10, pady = 10, rowspan = 7)
		self.scrollbar.config(command = self.book_list.yview)

		# Initialize list of contacts
		self.contact_list()

		#add contact button
		self.add_button = Tk.Button(master, text = 'Add', command = self.popupAdd)
		self.add_button.grid(row= 10, column = 0)

		#delete contact button
		self.delete_button = Tk.Button(master, text = 'Delete')#NEED TO ADD COMMAND
		self.delete_button.grid(row = 10, column = 1, sticky = Tk.W )

		#edit contact button
		self.edit_button = Tk.Button(master, text = 'Edit', command = self.popupEdit)
		self.edit_button.grid(row = 10, column = 6)

		#VIEW OF CONTACT INFO. ON THE LEFT SIDE OF THE WINDOW
		self.first_name_label = Tk.Label(master, text = 'First Name:')
		self.first_name_label.grid(row= 0, column = 3)

		#input for contacts first name
		self.first_name = Tk.Entry(master)
		self.first_name.grid(row = 0, column = 4)

		self.last_name_label = Tk.Label(master, text = 'Last Name:')
		self.last_name_label.grid(row = 1, column = 3) 

		#input for contacts last name
		self.last_name = Tk.Entry(master)
		self.last_name.grid(row = 1, column = 4)

		self.address1_label = Tk.Label(master, text = 'Address 1:')
		self.address1_label.grid(row = 2, column = 3, sticky = Tk.N)

		#input for contacts address1
		self.address1 = Tk.Entry(master)
		self.address1.grid(row = 2, column = 4, sticky = Tk.N )

		self.address2_label = Tk.Label(master, text = 'Address 2:')
		self.address2_label.grid(row = 3, column = 3)

		#input for contacts address2
		self.address2 = Tk.Entry(master)
		self.address2.grid(row = 3, column = 4)

		self.city_label = Tk.Label(master, text = 'City:')
		self.city_label.grid(row = 4, column = 3)

		#input for contacts city
		self.city = Tk.Entry(master)
		self.city.grid(row = 4, column = 4)

		self.state_label = Tk.Label(master, text = 'State:')
		self.state_label.grid(row = 5, column = 3)

		#input for contacts state
		self.state = Tk.Entry(master)
		self.state.grid(row = 5, column = 4 )

		self.zip_label = Tk.Label(master, text= 'Zip:')
		self.zip_label.grid(row = 6, column = 3)

		#input for the contacts zip
		self.zip = Tk.Entry(master)
		self.zip.grid(row = 6, column = 4)

		self.email_label = Tk.Label(master, text = 'e-Mail:')
		self.email_label.grid(row = 7, column = 3)

		#input for contacts email
		self.email = Tk.Entry(master)
		self.email.grid(row = 7, column = 4)

		self.birthday_label = Tk.Label(master, text = 'Birthday:')
		self.birthday_label.grid(row = 8, column = 3)

		#input for contacts birthday
		self.birthday = Tk.Entry(master)
		self.birthday.grid(row = 8, column = 4)

		self.notes_label = Tk.Label(master, text = "Notes")
		self.notes_label.grid(row = 9, column = 3)

		#input for notes on contact
		self.notes = Tk.Entry(master)
		self.notes.grid(row = 9, column = 4)


if __name__ == "__main__":
	master = Tk.Tk()
	m=mainWindow(master)
	w=AddContactWindow(master)
	k=EditContactWindow(master)
	n=New_AddBookWindow(master)
	master.mainloop()