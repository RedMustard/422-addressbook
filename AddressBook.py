"""
author: austin gheen
CIS422 Winter 2016

AddressBook.py
"""
import tkinter as Tk
import main as m

#  Need a function that initializes a new database upon application opening. i.e. when you
# 		input the name of the database, a call is made to add any existing entries into book_list
#  Check out field_return to see how the call is made to get_contacts()

class mainWindow(object):


	def field_return(self):
		r = self.item.get()
		m.add_contact(r)
		self.book_list.delete(0, Tk.END)
		for contact in m.get_contacts('last'):
			self.book_list.insert(Tk.END, contact)

	def popupNew_Addbook(self):
		self.n = New_AddBookWindow(self.master)
		self.master.wait_window(self.n.top)


	def popupAdd(self):
		self.w=AddContactWindow(self.master)
		self.master.wait_window(self.w.top)

	def popupEdit(self):
		self.k=EditContactWindow(self.master)
		self.master.wait_window(self.k.top)


	def __init__(self,master):
		self.master = master
		master.title('Address Book')

		#entry field
		self.item = Tk.Entry(master)
		self.item.grid(row=0, column = 1, pady = 10)
		self.item.insert(0, 'Enter name')

		#submit button
		self.submit = Tk.Button(master, text='Submit', command = self.field_return)
		self.submit.grid(row = 1, column = 1)

		#new address book button
		self.new_button = Tk.Button(master, text='New', command = self.popupNew_Addbook)
		self.new_button.grid(row = 1, column = 2)


		#scroll bar and box list of contacts
		self.scrollbar = Tk.Scrollbar(master)
		self.scrollbar.grid(row = 2, column = 2)
		self.book_list = Tk.Listbox(master, yscrollcommand = self.scrollbar.set)
		self.book_list.grid(row = 2, column = 1, padx = 10, pady = 10, rowspan = 7)
		self.scrollbar.config(command = self.book_list.yview)

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




class AddContactWindow(object):

	def field_return(self):
		"""Grabs form data and creates"""

		field_list = ['','','','','','','','','','','','']


		
		# field_names = ['first_name', 'last_name', 'address1', 'address2', 
		# 		'city', 'state', 'zip', 'home', 'mobile', 'email', 'birthday']

		# i = 0
		# for field in field_vars:
		# 	field = self.{}.format(field_names[i]).get()
		# 	i += 1


		first = self.first_name.get()
		last = self.last_name.get()
		st1 = self.address1.get()
		st2 = self.address2.get()
		city = self.city.get()
		state = self.state.get()
		zip = self.zip.get()
		home = self.home.get()
		mobile = self.mobile.get()
		email = self.email.get()
		bday = self.birthday.get()
		notes = self.notes.get()

		field_vars = [first, last, st1, st2, city, state, zip, home, mobile, email, bday, notes]

		for i in range(12):
			field_list[i] = field_vars[i]

		# for i in field_list:
		# 	print(i)

		m.add_contact(field_list)
		

		# self.book_list.delete(0, Tk.END)


		# for contact in m.get_contacts('last'):
		# 	mainWindow.__init__.book_list.insert(Tk.END, contact)



	def __init__(self,master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title('Add Contact')

		self.first_name_label = Tk.Label(top, text = 'First Name:')
		self.first_name_label.grid()

		#input for contacts first name
		self.first_name = Tk.Entry(top)
		self.first_name.grid(row = 0, column = 1)

		self.last_name_label = Tk.Label(top, text = 'Last Name:')
		self.last_name_label.grid(row = 1) 

		#input for contacts last name
		self.last_name = Tk.Entry(top)
		self.last_name.grid(row = 1, column = 1)

		self.address1_label = Tk.Label(top, text = 'Address 1:')
		self.address1_label.grid(row = 2)

		#input for contacts address1
		self.address1 = Tk.Entry(top)
		self.address1.grid(row = 2, column = 1)

		self.address2_label = Tk.Label(top, text = 'Address 2:')
		self.address2_label.grid(row = 3)

		#input for contacts address2
		self.address2 = Tk.Entry(top)
		self.address2.grid(row = 3, column = 1)

		self.city_label = Tk.Label(top, text = 'City:')
		self.city_label.grid(row = 4)

		#input for contacts city
		self.city = Tk.Entry(top)
		self.city.grid(row = 4, column = 1)

		self.state_label = Tk.Label(top, text = 'State:')
		self.state_label.grid(row = 5)

		#input for contacts state
		self.state = Tk.Entry(top)
		self.state.grid(row = 5, column = 1 )

		self.zip_label = Tk.Label(top, text= 'Zip:')
		self.zip_label.grid(row = 6)

		#input for the contacts zip
		self.zip = Tk.Entry(top)
		self.zip.grid(row = 6, column = 1)

		# Input for contact home phone
		self.home_label = Tk.Label(top, text = 'Home Phone:')
		self.home_label.grid(row = 7)

		self.home = Tk.Entry(top)
		self.home.grid(row = 7, column = 1)

		# Input for contact mobile phone
		self.mobile_label = Tk.Label(top, text = 'Home Phone:')
		self.mobile_label.grid(row = 8)

		self.mobile = Tk.Entry(top)
		self.mobile.grid(row = 8, column = 1)
		
		self.email_label = Tk.Label(top, text = 'e-mail:')
		self.email_label.grid(row = 9)

		#input for contacts email
		self.email = Tk.Entry(top)
		self.email.grid(row = 9, column = 1)

		self.birthday_label = Tk.Label(top, text = 'Birthday:')
		self.birthday_label.grid(row = 10)

		#input for contacts birthday
		self.birthday = Tk.Entry(top)
		self.birthday.grid(row = 10, column = 1)

		self.notes_label = Tk.Label(top, text = "Notes")
		self.notes_label.grid(row = 11)

		#input for notes on contact
		self.notes = Tk.Entry(top)
		self.notes.grid(row = 11, column = 1)

		self.add_button = Tk.Button(top, text= 'Add', command = self.field_return)#NEED TO MAKE BUTTON FUNCTIONAL
		self.add_button.grid(row = 12, column = 2)

		self.cancel_button = Tk.Button(top, text = 'Cancel')#NEED TO MAKE BUTTON FUNCTIONAL
		self.cancel_button.grid(row = 13, column = 2)

class EditContactWindow(object):
	"""
	def field_return(self):
		#Grabs form data and creates

		field_list = ['','','','','','','','','','','','']

		first = self.first_name.get()
		last = self.last_name.get()
		st1 = self.address1.get()
		st2 = self.address2.get()
		city = self.city.get()
		state = self.state.get()
		zip = self.zip.get()
		home = self.home.get()
		mobile = self.mobile.get()
		email = self.email.get()
		bday = self.birthday.get()
		notes = self.notes.get()

		field_vars = [first, last, st1, st2, city, state, zip, home, mobile, email, bday, notes]

		for i in range(12):
			field_list[i] = field_vars[i]

		m.add_contact(field_list)
	"""

	def __init__(self, master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title('Edit Contact')

		self.first_name_label = Tk.Label(top, text = 'First Name:')
		self.first_name_label.grid()

		#input for contacts first name
		self.first_name = Tk.Entry(top)
		self.first_name.grid(row = 0, column = 1)

		self.last_name_label = Tk.Label(top, text = 'Last Name:')
		self.last_name_label.grid(row = 1) 

		#input for contacts last name
		self.last_name = Tk.Entry(top)
		self.last_name.grid(row = 1, column = 1)

		self.address1_label = Tk.Label(top, text = 'Address 1:')
		self.address1_label.grid(row = 2)

		#input for contacts address1
		self.address1 = Tk.Entry(top)
		self.address1.grid(row = 2, column = 1)

		self.address2_label = Tk.Label(top, text = 'Address 2:')
		self.address2_label.grid(row = 3)

		#input for contacts address2
		self.address2 = Tk.Entry(top)
		self.address2.grid(row = 3, column = 1)

		self.city_label = Tk.Label(top, text = 'City:')
		self.city_label.grid(row = 4)

		#input for contacts city
		self.city = Tk.Entry(top)
		self.city.grid(row = 4, column = 1)

		self.state_label = Tk.Label(top, text = 'State:')
		self.state_label.grid(row = 5)

		#input for contacts state
		self.state = Tk.Entry(top)
		self.state.grid(row = 5, column = 1 )

		self.zip_label = Tk.Label(top, text= 'Zip:')
		self.zip_label.grid(row = 6)

		#input for the contacts zip
		self.zip = Tk.Entry(top)
		self.zip.grid(row = 6, column = 1)

		# Input for contact home phone
		self.home_label = Tk.Label(top, text = 'Home Phone:')
		self.home_label.grid(row = 7)

		self.home = Tk.Entry(top)
		self.home.grid(row = 7, column = 1)

		# Input for contact mobile phone
		self.mobile_label = Tk.Label(top, text = 'Home Phone:')
		self.mobile_label.grid(row = 8)

		self.mobile = Tk.Entry(top)
		self.mobile.grid(row = 8, column = 1)
		
		self.email_label = Tk.Label(top, text = 'e-mail:')
		self.email_label.grid(row = 9)

		#input for contacts email
		self.email = Tk.Entry(top)
		self.email.grid(row = 9, column = 1)

		self.birthday_label = Tk.Label(top, text = 'Birthday:')
		self.birthday_label.grid(row = 10)

		#input for contacts birthday
		self.birthday = Tk.Entry(top)
		self.birthday.grid(row = 10, column = 1)

		self.notes_label = Tk.Label(top, text = "Notes")
		self.notes_label.grid(row = 11)

		#input for notes on contact
		self.notes = Tk.Entry(top)
		self.notes.grid(row = 11, column = 1)

		self.add_button = Tk.Button(top, text= 'Save')#, command = #save function)#NEED TO MAKE BUTTON FUNCTIONAL
		self.add_button.grid(row = 12, column = 2)

		self.cancel_button = Tk.Button(top, text = 'Cancel')#NEED TO MAKE BUTTON FUNCTIONAL
		self.cancel_button.grid(row = 13, column = 2)

class New_AddBookWindow(object):

	#function for when Ok button is pressed
	#def Ok():

	def __init__(self, master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title('New Address Book')

		self.instruction_message = Tk.Label(top, text = 'Please enter the name of\n your new address book')
		self.instruction_message.grid()

		self.book_name_label = Tk.Label(top, text = 'Address Book Name:')
		self.book_name_label.grid(row = 1)

		#entry is for user's desired Address Book Name
		self.book_name = Tk.Entry(top)
		self.book_name.grid(row = 1 , column = 1, padx = 10, pady = 10)

		self.cancel_button = Tk.Button(top, text = 'Cancel')#, command = cancel_command) #NEED TO MAKE BUTTON FUNCTIONAL
		self.cancel_button.grid(row = 2, column = 2)

		self.ok_button = Tk.Button(top, text= 'Ok')#, command = ok_command)#NEED TO MAKE BUTTON FUNCTIONAL
		self.ok_button.grid(row = 2, column = 3)


if __name__ == "__main__":
	master = Tk.Tk()
	m=mainWindow(master)
	w=AddContactWindow(master)
	k=EditContactWindow(master)
	n=New_AddBookWindow(master)
	master.mainloop()