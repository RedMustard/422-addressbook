"""Address Book GUI

Authors: Austin Gheen, Travis Barnes, Brandon Cao
CIS422 Winter 2016

AddressBook.py
"""
import sys
sys.path.insert(0, '..')

import tkinter as Tk
import AddressBook as ab
import db
import new # New address book window
import ecw # Edit Contact Window
import acw # Add Contact Window
import dcw  # Confirmation Window

#  Need a function that initializes a new database upon application opening. i.e. when you
# 		input the name of the database, a call is made to add any existing entries into book_list
#  Check out field_return to see how the call is made to get_contacts_list()

class mainWindow(object):

	def close_window(self):
		self.top.destroy()


	# def contact_list(self, sort):
	# 	"""Retrieves list of contacts"""
	# 	self.book_list.delete(0, Tk.END)

	# 	for contact in ab.get_contacts_list(self.sort.get()):
	# 		self.book_list.insert(Tk.END, contact[0] + " " + contact[1])
			
	def search_call(self):
		""" """
		self.search_query(self.sort.get())



	def search_query(self, sort):
		""" """
		self.book_list.delete(0, Tk.END)

		for contact in ab.search(self.search_bar.get(), sort):
			self.book_list.insert(Tk.END, contact[0] + " " + contact[1])

	def delete_contact(self, name):
		"""Deletes selected contact"""
		ab.remove_contact(name)
		self.search_query(self.sort.get())


	def field_return(self):
		i = 0
		r = self.item.get()
		ab.add_contact(r)
		self.book_list.delete(0, Tk.END)
		for contact in ab.get_contacts_list('last'):
			self.book_list.insert(Tk.END, contact[0]+contact[1])

	def popupNew_Addbook(self):
		newWindow = Tk.Toplevel(self.master)
		self.n = new.New_AddBookWindow(newWindow)
		self.master.wait_window(self.n.top)


	def popupAdd(self):
		self.w=acw.AddContactWindow(self.master)
		self.master.wait_window(self.w.top)


	def popupEdit(self):
		name = str(self.book_list.get(self.book_list.curselection()))
		entry = []

		try:
			entry.append(name.split()[0])
		except:
			entry.append('')

		try:
			entry.append(name.split()[1])
		except:
			entry.append('');

		entry_id = db.get_id(entry)
		self.k=ecw.EditContactWindow(self.master, name, entry_id)
		self.master.wait_window(self.k.top)


	def popup_confirmation(self):
		name = str(self.book_list.get(self.book_list.curselection()))
		self.c=dcw.ConfirmationWindow(self.master, name)
		self.master.wait_window(self.c.top)


	def open(self):
		print('open')


	def save(self):
		print('save')

	def quit(self):
		sys.exit()

	def noEdit(self):
		self.first_name.configure(state='readonly')
		self.last_name.configure(state='readonly')
		self.address1.configure(state='readonly')
		self.address2.configure(state='readonly')
		self.city.configure(state='readonly')
		self.state.configure(state='readonly')
		self.zip.configure(state='readonly')
		self.home.configure(state='readonly')
		self.mobile.configure(state='readonly')
		self.email.configure(state='readonly')
		self.birthday.configure(state='readonly')
		self.notes.configure(state='readonly')


	def onSelect(self,event):
		"""Grabs name from contact list upon user click."""
		w = event.widget
		name = str(self.book_list.get(self.book_list.curselection()))
		self.clearTextEntries()
		# print(name)
		name_entry = ab.get_contact(name)
		# print(name_entry)
		self.first_name.insert(0,str(name_entry[0]))
		self.last_name.insert(0,str(name_entry[1]))
		self.address1.insert(0,str(name_entry[2]))
		self.address2.insert(0,str(name_entry[3]))
		self.city.insert(0,str(name_entry[4]))
		self.state.insert(0,str(name_entry[5]))
		self.zip.insert(0,str(name_entry[6]))
		self.home.insert(0,str(name_entry[7]))
		self.mobile.insert(0,str(name_entry[8]))
		self.email.insert(0,str(name_entry[9]))
		self.birthday.insert(0,str(name_entry[10]))
		self.notes.insert(0,str(name_entry[11]))

		#User cannot edit entry displayed on main GUI, unless clicking edit button. 
		self.first_name.configure(state='readonly')
		self.last_name.configure(state='readonly')
		self.address1.configure(state='readonly')
		self.address2.configure(state='readonly')
		self.city.configure(state='readonly')
		self.state.configure(state='readonly')
		self.zip.configure(state='readonly')
		self.home.configure(state='readonly')
		self.mobile.configure(state='readonly')
		self.email.configure(state='readonly')
		self.birthday.configure(state='readonly')
		self.notes.configure(state='readonly')



	def clearTextEntries(self):
		"""Clears any value in text fields. For use when user selects different contact"""
		self.first_name.configure(state='normal')
		self.last_name.configure(state='normal')
		self.address1.configure(state='normal')
		self.address2.configure(state='normal')
		self.city.configure(state='normal')
		self.state.configure(state='normal')
		self.zip.configure(state='normal')
		self.home.configure(state='normal')
		self.mobile.configure(state='normal')
		self.email.configure(state='normal')
		self.birthday.configure(state='normal')
		self.notes.configure(state='normal')


		self.first_name.delete(0,Tk.END)
		self.last_name.delete(0,Tk.END)
		self.address1.delete(0,Tk.END)
		self.address2.delete(0,Tk.END)
		self.city.delete(0,Tk.END)
		self.state.delete(0,Tk.END)
		self.zip.delete(0,Tk.END)
		self.home.delete(0,Tk.END)
		self.mobile.delete(0,Tk.END)
		self.email.delete(0,Tk.END)
		self.birthday.delete(0,Tk.END)
		self.notes.delete(0,Tk.END)


	def __init__(self,master):
		self.master = master
		master.title('Address Book')

		#Menu bar
		menuBar = Tk.Menu(self.master)
		options = Tk.Menu(menuBar, tearoff=0)
		#File tab
		options.add_command(label="New", command=lambda:function)
		options.add_command(label="Open", command=lambda:function)
		options.add_command(label="Close", command=lambda:function)
		options.add_command(label="Save", command=lambda:function)
		options.add_command(label="Save as..", command=lambda:function)
		options.add_command(label="Close", command= self.quit)
		options.add_separator()
		menuBar.add_cascade(label="File", menu=options)

		#Help tab
		helpOptions = Tk.Menu(menuBar, tearoff=1)
		helpOptions.add_command(label="Help Documentation", command=lambda:function)
		helpOptions.add_command(label="About", command=lambda:function)
		helpOptions.add_separator()
		menuBar.add_cascade(label="Help", menu=helpOptions)
		
		self.master.config(menu=menuBar)

		#new address book button
		self.new_button = Tk.Button(master, text='New', command = self.popupNew_Addbook)
		self.new_button.grid(row = 0, column = 0, sticky = Tk.W, padx = 15, pady = 10 )

		#open address book button
		self.open_button = Tk.Button(master, text="Open", command = self.open )
		self.open_button.grid(row = 0, column = 0, sticky = Tk.E, padx= 0)

		#sort option menu default option
		self.sort = Tk.StringVar(master)
		self.sort.set('Last Name')

		#sort option menu #self.sort.get() to get the value of user's option
		self.sort_option_menu = Tk.OptionMenu(master, self.sort, 'Last Name', 'Zip', command = self.search_query)# , 'option' #to add another option
		self.sort_option_menu.grid(row = 1, column = 0, sticky = Tk.W, padx = 10)

		#scroll bar and box list of contacts
		self.scrollbar = Tk.Scrollbar(master)
		self.scrollbar.grid(row = 2, column = 1)
		self.book_list = Tk.Listbox(master, yscrollcommand = self.scrollbar.set, height=20)
		self.book_list.grid(row = 2, column = 0, rowspan = 12 , padx = 15)
		self.scrollbar.config(command = self.book_list.yview)
		self.book_list.bind('<<ListboxSelect>>', self.onSelect)
		
		#search bar
		self.search_bar = Tk.Entry(master)
		self.search_bar.grid(row = 0, column = 4, padx = 10 )
		self.search_bar.insert(0, '')

		self.search_return = Tk.Button(master, text = 'Search', command = self.search_call)
		self.search_return.grid(row = 0, column = 5, padx = 5)

		# Initialize list of contacts
		# self.contact_list(self.sort.get())
		self.search_query(self.sort.get())

		#add contact button
		self.add_button = Tk.Button(master, text = 'Add', command = self.popupAdd)
		self.add_button.grid(row = 14, column = 0, sticky = Tk.W , padx = 12 ) 

		#delete contact button
		self.delete_button = Tk.Button(master, text = 'Delete', command = self.popup_confirmation )
		self.delete_button.grid(row = 14, column = 0 )

		#edit contact button
		self.edit_button = Tk.Button(master, text = 'Edit', command = self.popupEdit)
		self.edit_button.grid(row = 14, column = 4, padx = 10, sticky = Tk.E )

		#VIEW OF CONTACT INFO. ON THE RIGHT SIDE OF THE WINDOW
		self.first_name_label = Tk.Label(master, text = 'First Name:')
		self.first_name_label.grid(row= 2, column = 3)

		#input for contacts first name
		self.first_name = Tk.Entry(master)
		self.first_name.grid(row = 2, column = 4)

		self.last_name_label = Tk.Label(master, text = 'Last Name:')
		self.last_name_label.grid(row = 3, column = 3) 

		#input for contacts last name
		self.last_name = Tk.Entry(master)
		self.last_name.grid(row = 3, column = 4)

		self.address1_label = Tk.Label(master, text = 'Address 1:')
		self.address1_label.grid(row = 4, column = 3)

		#input for contacts address1
		self.address1 = Tk.Entry(master)
		self.address1.grid(row = 4, column = 4)

		self.address2_label = Tk.Label(master, text = 'Address 2:')
		self.address2_label.grid(row = 5, column = 3)

		#input for contacts address2
		self.address2 = Tk.Entry(master)
		self.address2.grid(row = 5, column = 4)

		self.city_label = Tk.Label(master, text = 'City:')
		self.city_label.grid(row = 6, column = 3)

		#input for contacts city
		self.city = Tk.Entry(master)
		self.city.grid(row = 6, column = 4)

		self.state_label = Tk.Label(master, text = 'State:')
		self.state_label.grid(row = 7, column = 3)

		#input for contacts state
		self.state = Tk.Entry(master)
		self.state.grid(row = 7, column = 4 )

		self.zip_label = Tk.Label(master, text= 'Zip:')
		self.zip_label.grid(row = 8, column = 3)

		#input for the contacts zip
		self.zip = Tk.Entry(master)
		self.zip.grid(row = 8, column = 4)


		# Home phone
		self.home_label = Tk.Label(master, text = 'Home:')
		self.home_label.grid(row = 9, column = 3)
		self.home = Tk.Entry(master)
		self.home.grid(row = 9, column = 4)

		# Mobile phone
		self.mobile_label = Tk.Label(master, text = 'Mobile:')
		self.mobile_label.grid(row = 10, column = 3)
		self.mobile = Tk.Entry(master)
		self.mobile.grid(row = 10, column = 4)

		self.email_label = Tk.Label(master, text = 'Email:')
		self.email_label.grid(row = 11, column = 3)

		#input for contacts email
		self.email = Tk.Entry(master)
		self.email.grid(row = 11, column = 4)

		self.birthday_label = Tk.Label(master, text = 'Birthday:')
		self.birthday_label.grid(row = 12, column = 3)

		#input for contacts birthday
		self.birthday = Tk.Entry(master)
		self.birthday.grid(row = 12, column = 4)

		self.notes_label = Tk.Label(master, text = "Notes")
		self.notes_label.grid(row = 13, column = 3 )

		#input for notes on contact
		self.notes = Tk.Entry(master)
		self.notes.grid(row = 13, column = 4)
		
		self.noEdit()

if __name__ == "__main__":
	master = Tk.Tk()
	m=mainWindow(master)
	w=AddContactWindow(master)
	k=EditContactWindow(master)
	n=New_AddBookWindow(master)
	c=ConfirmationWindow(master)
	master.mainloop()


