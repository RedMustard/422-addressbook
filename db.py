"""Address Book Database

Author: Travis Barnes, January 16 2016

This program creates, modifies (insert, delete, update),  and queries a
SQLite database filled with address book entries.
"""

import sqlite3 as sql
import os.path as path
import config as cfg


def db_init(argv):
	"""Create and initialize a new database.

	Keyword arguments:
	argv -- Name of the new database file
	"""	

	if db_exists(argv) == True:
		cfg.DB = sql.connect(argv)
		cfg.C = cfg.DB.cursor()
		print('no table creation')

	else:
		cfg.DB = sql.connect(argv)
		cfg.C = cfg.DB.cursor()
		create_table = '''CREATE TABLE Contacts(ID TEXT PRIMARY KEY, First TEXT, 
					Last TEXT, Home TEXT, Mobile TEXT, Email TEXT, 
					Street1 TEXT, Street2 TEXT, City TEXT, State TEXT, 
					Zip TEXT, Birthday TEXT, Notes TEXT) '''	
		cfg.C.execute(create_table)
		cfg.DB.commit()
		print('table creation')
	

def db_exists(argv):
	"""Checks whether db exists.

	Keyword arguments:
	argv -- Name of a database file
	"""

	if (path.isfile(argv)):
		return True
	else:
		return False
		

# def get_entry():
# 	"""Turn user input into a list object.

# 	Keyword returns:
# 	entry -- A list object
# 	"""


def insert_contact(entry):
	"""Inserts a new entry into database.

	Keyword arguments:
	entry -- A list object 
	"""

	cfg.C.execute('INSERT INTO Contacts VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', entry,)

	cfg.DB.commit()


def delete_contact(id):
	"""Removes entry from database.

	Keyword arguments:
	id -- Corresponding ID number for a database entry.
	"""

	delete = "DELETE FROM Contacts WHERE ID LIKE '%'|| ? || '%' "
	cfg.C.execute(delete, [id],)

	del_confirm = input("Are you sure you want to delete the contact? (Y/N)")

	if del_confirm == 'y' or del_confirm == 'Y':
		cfg.DB.commit()


# def edit_contact(id):
# 	"""Updates entry in database.

# 	Keyword arguments:
# 	id -- Corresponding ID number for a database entry.
# 	"""


def query_namelist():
	"""Prints the full list of entries in database."""

	query = "SELECT * FROM Contacts"
	cfg.C.execute(query)

	for row in cfg.C:
		print(row)


# def sort_namelist():
# 	"""Sorts the namelist."""


# def entry_search(entry):
# 	"""Searches the database for an entry."""


# def input_validation(entry):
# 	"""Validates user input to make sure it is in proper format."""


if __name__ == "__main__":
	entry = ['0', 'Travis', 'Barnes', '555-555-5555', '555-444-4444', 'ttb@uoregon.edu', 'street ad1',
				'street ad2', 'Eugene', 'OR', '52642', '08/30/1991', 'Insert notes here']

	entry2 = ['1', 'George', 'Castanza', '555-333-3333', '', 'castanza@seinfeld.com', '5th street',
				'', 'NYC', 'NY', '11111', '', '']

	filename = input("Enter the name of the address book file: \n")
	print("Creating database... \n")
	db_init(filename)
	print("Database opened.\n")

	print("Printing contacts...\n")
	query_namelist()

	print("Inserting contacts... \n")
	insert_contact(entry)
	insert_contact(entry2)
	print("Printing contacts...\n")
	query_namelist()

	print("Deleting contact 0... \n")
	delete_contact('0')
	print("Printing contacts...\n")
	query_namelist()
