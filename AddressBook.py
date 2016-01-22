"""Main Address Book application 

Author: Travis Barnes, 18 January 2016

"""

import sys
sys.path.insert(0, 'GUI')

import gui as gui
import db
import tkinter as Tk

def get_contacts_list(sort):
	"""
	"""
	contacts = []
	for row in (db.query_entrylist(sort)):
		contacts.append(row)
	return contacts
	

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
	# print(create_contact(contact))
	db.insert_entry(contact)


def remove_contact():
	"""Removes a contact"""


def edit_contact():
	"""Edits a contact"""


def new_book():
	"""Creates a new address book"""
	book_name = input("Enter the name of your new address book: ")
	return (db.db_init(book_name))

def open_book():
	"""Opens an exisitng address book"""


if __name__ == "__main__":
    new_book()
    root = Tk.Tk()
    gui.mainWindow(root)
    root.mainloop()
    # gui.root.mainloop()
	