"""Main Address Book application 

Author: Travis Barnes, 18 January 2016

"""

import sys
sys.path.insert(0, 'GUI')

import tkinter as Tk
import gui
import db
import new


# def get_contacts_list(sort):
# 	"""
# 	"""
# 	contacts = []
	
# 	for row in (db.query_entrylist(sort)):
# 		contacts.append(row)

# 	return contacts


def get_contact(contact):
	"""
	"""
	entry = []

	try:
		try:
			if contact.split()[1]:
				entry.append(contact.split()[0])
				print("some	")
		except:
			print('thing')
			entry.append('')

	except:
		entry.append('')

	try:
		entry.append(contact.split()[1])
	except:
		entry.append('');

	for row in db.get_entry(db.get_id(entry)):
		return row


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
	print(entry)
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


def edit_contact(entry_id, contact):
	"""Edits a contact"""
	db.edit_entry(entry_id, contact)


def search(search_string, sort):
	"""Searches the database and returns the results"""
	return db.search_entry(search_string, sort)


def new_book():
	"""Creates a new address book"""
	book_name = input("Enter the name of your new address book: ")
	return (db.db_init(book_name))


def open_book():
	"""Opens an exisitng address book"""


if __name__ == "__main__":
    root = Tk.Tk()
    new.New_AddBookWindow(root)
    root.mainloop()


    # gui.root.mainloop()
	