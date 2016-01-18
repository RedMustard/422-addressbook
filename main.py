"""Main Address Book application 

Author: Travis Barnes, 18 January 2016


"""

import AddressBook as ab
import db

def get_contacts(sort):
	"""
	"""
	contacts = []
	for row in (db.query_entrylist(sort)):
		contacts.append(row)
	return contacts
	# return db.query_entrylist(sort)
	

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
	db.insert_entry(create_contact(contact))


def remove_contact():
	"""Removes a contact"""


def edit_contact():
	"""Edits a contact"""


def new_book():
	"""Creates a new address book"""
	book_name = input("Enter the name of your new address book: ")
	return (db.db_init(book_name))


if __name__ == "__main__":
	new_book()
	ab.root.mainloop()
	