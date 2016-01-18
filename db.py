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
		print('DB exists')

	else:
		cfg.DB = sql.connect(argv)
		cfg.C = cfg.DB.cursor()
		create_table = '''CREATE TABLE Contacts(ID TEXT PRIMARY KEY, First TEXT, 
					Last TEXT, Home TEXT, Mobile TEXT, Email TEXT, 
					Street1 TEXT, Street2 TEXT, City TEXT, State TEXT, 
					Zip TEXT, Birthday TEXT, Notes TEXT) '''	
		cfg.C.execute(create_table)
		cfg.DB.commit()
		print('Table created')
	

def db_exists(argv):
	"""Checks whether db exists.

	Keyword arguments:
	argv -- Name of a database file
	"""

	if (path.isfile(argv)):
		return
	else:
		return False


# def get_entry():
# 	"""Turn user input into a list object.

# 	Keyword returns:
# 	entry -- A list object
# 	"""


def insert_entry(entry):
	"""Inserts a new entry into database.

	Keyword arguments:
	entry -- A list object 
	"""

	cfg.C.execute('INSERT INTO Contacts VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', 
		entry,)

	cfg.DB.commit()


def delete_entry(id):
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


def query_entrylist(argv):
	"""Prints the full list of entries in database."""

	# Choose the sorting option
	if argv == 'last':
		last_name = '''SELECT * FROM Contacts ORDER BY Last'''
		cfg.C.execute(last_name)

	elif argv == 'zip':
		zip_code = '''SELECT * FROM Contacts ORDER BY Zip'''
		cfg.C.execute(zip_code)

	for row in cfg.C:
		print(row)



# def entry_search(entry):
# 	"""Searches the database for an entry."""


# def input_validation(entry):
# 	"""Validates user input to make sure it is in proper format."""


if __name__ == "__main__":
	entry0 = ['0', 'Travis', 'Barnes', '555-555-5555', '555-444-4444', 'ttb@uoregon.edu', 'street ad1',
				'street ad2', 'Eugene', 'OR', '11111', '08/30/1991', 'Insert notes here']

	entry1 = ['1', 'George', 'Castanza', '555-333-3333', '', 'castanza@seinfeld.com', '5th street',
				'', 'NYC', 'NY', '11111', '', '']

	entry2 = ['2', 'Giacomo', 'Ouillizzoni', '555-222-2222', '', 'gguillizzoni@mail.com', '123 Fake St.',
				'Apt 7', 'FakeTown', 'FakeState', '33333', '', 'Cool dude.']

	entry3 = ['3', 'Thomas', 'Mark', '555-777-7777', '', 'markt@mail.com', '',
				'', 'City', 'State', '33333', '', '']

	filename = input("Enter the name of the address book file: ")
	print("Creating database...")
	db_init(filename)
	print("Database opened.\n")

	print("Printing contacts...")
	query_entrylist('last')

	print("Inserting contacts...")
	insert_entry(entry0)
	insert_entry(entry1)
	insert_entry(entry2)
	insert_entry(entry3)
	print("Printing contacts...")
	query_entrylist('last')

	print("\nDeleting contact 0... ")
	delete_entry('0')
	print("Printing contacts...")
	query_entrylist('last')

	print("Inserting contacts... \n")
	insert_entry(entry0)
	print("Printing contacts...\n")
	query_entrylist('last')

	print("Sorting contacts by zip code..\n")
	query_entrylist('zip')
