"""
Address Book database

Author: Travis Barnes, January 16 2016

This program creates, modifies (insert, delete, update),  and queries a
SQLite database filled with address book entries.
"""

import sqlite3 as sql

DB = sql.connect('test')
C = DB.cursor()

def db_init(argv):
	"""
	Given a nonexistent database, creates the necessary table to store address 
	book entries.
	"""	

	DB = sql.connect(argv)
	
	create_table = '''CREATE TABLE Contacts(ID TEXT PRIMARY KEY, First TEXT, 
					Last TEXT, Home TEXT, Mobile TEXT, Email TEXT, 
					Street1 TEXT, Street2 TEXT, City TEXT, State TEXT, 
					Zip TEXT, Birthday TEXT, Notes TEXT) '''
	C.execute(create_table)
	

def get_entry():
	"""
	Grabs user input from address book fields and turns into a list object.
	"""


def insert_contact(entry):
	"""
	Inserts a new contact entry into database.
	"""

	C.execute('INSERT INTO Contacts VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', entry,)

	DB.commit()


def delete_contact(id):
	"""
	Searches for contact in database and removes it.
	"""

	delete = "DELETE FROM Contacts WHERE ID LIKE '%'|| ? || '%' "
	C.execute(delete, [id],)

	del_confirm = input("Are you sure you want to delete the contact? (Y/N)")

	if del_confirm == 'y' or del_confirm == 'Y':
		DB.commit()


def edit_contact(name):
	"""
	Searches for contact in database and 
	"""


def query_namelist():
	"""
	Queries the database and returns the full list of contacts.
	"""
	query = "SELECT * FROM Contacts"
	C.execute(query)

	for row in C:
		print(row)


def sort_namelist():
	"""
	Sorts the namelist.
	"""


def entry_search(entry):
	"""
	Searches the database for an entry.
	"""


def input_validation(entry):
	"""
	Validates user input to make sure it is in proper format.
	"""


if __name__ == "__main__":
	entry = ['0', 'Travis', 'Barnes', '555-555-5555', '555-444-4444', 'ttb@uoregon.edu', 'street ad1',
			'street ad2', 'Eugene', 'OR', '52642', '08/30/1991', 'Insert notes here']

	print("Creating table... \n")
	# db_init('test')
	print("Insert Contact: \n")
	# insert_contact()
	query_namelist()
	print("Delete Contact: \n")
	delete_contact('0')
	query_namelist()
