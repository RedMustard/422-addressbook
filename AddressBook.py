"""Main Address Book application 

Author: Travis Barnes, 18 January 2016

"""

import sys
sys.path.insert(0, 'GUI')

import tkinter as Tk
import gui
import db


def get_contacts_list(sort):
	"""
	"""
	contacts = []
	
	for row in (db.query_entrylist(sort)):
		contacts.append(row)

	return contacts

def get_contact(contact):
	"""
	"""
	entry = []

	try:
		entry.append(contact.split()[0])
	except:
		entry.append('')

	try:
		entry.append(contact.split()[1])
	except:
		entry.append('');

	# print(db.get_id(entry))

	for row in db.get_entry(db.get_id(entry)):
		return row

	# print(entry)

	

def create_contact(contact):
	"""Eventually add First, Last, Street1, ...."""
	entry = []
	entry.append(contact)
	entry.append('') 
	entry.append('')
	entry.append('')
	entry.append('')
	entry.append('')
	entry.append('')
	entry.append('')
	entry.append('')
	entry.append('')
	entry.append('')
	entry.append('')
	return entry

def add_contact(contact):
	"""Adds a contact to the database"""
	db.insert_entry(contact)


def remove_contact(contact):
	"""Removes a contact"""
	entry = []
	try:
		entry.append(contact.split()[0])
	except:
		entry.append('')

	try:
		entry.append(contact.split()[1])
	except:
		entry.append('');
	
	db.delete_entry(db.get_id(entry))


def edit_contact(contact):
	"""Edits a contact"""

	db.edit_entry(db.get_id((contact[0] + contact[1])), contact)


def new_book():
	"""Creates a new address book"""
	## WINDOW POPS UP HERE ##
	book_name = input("Enter the name of your new address book: ")
	return (db.db_init(book_name)) ## <----- PASS USER INPUT   book_name

def open_book():
	"""Opens an exisitng address book"""


if __name__ == "__main__":
    new_book()
    root = Tk.Tk()
    gui.mainWindow(root)
    root.mainloop()

    # gui.root.mainloop()
	