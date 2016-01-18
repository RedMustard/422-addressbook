"""Address Book Database

Author: Travis Barnes, January 16 2016

This program creates, modifies (insert, delete, update), and queries a
SQLite database filled with address book entries.
"""

import sqlite3 as sql
import os.path as path
import config as cfg


def db_init(db_name):
	"""Create/Open and initialize a database.

	Keyword arguments:
	db_name -- Name of the new database file
	"""	

	if db_exists(db_name) == True:
		cfg.DB = sql.connect(db_name + '.ab')
		cfg.C = cfg.DB.cursor()
		print('Database already exists')

	else:
		cfg.DB = sql.connect(db_name + '.ab')
		cfg.C = cfg.DB.cursor()
		create_table = '''CREATE TABLE Contacts(First TEXT, 
					Last TEXT, Street1 TEXT, Street2 TEXT, City TEXT, State TEXT,
					Zip TEXT, Home TEXT, Mobile TEXT, Email TEXT, Birthday TEXT, 
					Notes TEXT) '''	
		cfg.C.execute(create_table)
		cfg.DB.commit()
		print('New table created')
	

def db_exists(db_name):
	"""Checks whether db exists.

	Keyword arguments:
	db_name -- Name of a database file
	"""

	if (path.isfile(db_name + '.ab')):
		return True
	else:
		return False


def get_id(entry):
	"""Gets database ID number from an entry

	Keyword arguments:
	entry - A list object
	"""
	entry_id = "SELECT rowid, * FROM Contacts WHERE First = ? AND Last = ?"
	cfg.C.execute(entry_id, [entry[0], entry[1]])

	for row in cfg.C:
		return row[0]


def create_entry(first, last, st1, st2, city, st, zip, home, mob, email, bday, 
	note):
	"""Creates an entry list object.

	Keyword returns:
	entry -- A list object
	"""

	entry = []

	entry.append(first)
	entry.append(last) 
	entry.append(st1)
	entry.append(st2)
	entry.append(city)
	entry.append(st)
	entry.append(zip)
	entry.append(home)
	entry.append(mob)
	entry.append(email)
	entry.append(bday)
	entry.append(note)

	return entry


def insert_entry(entry):
	"""Inserts a new entry into database.

	Keyword arguments:
	entry -- A list object 
	"""

	cfg.C.execute('INSERT INTO Contacts VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
		entry)

	cfg.DB.commit()


def delete_entry(entry):
	"""Removes entry from database.

	Keyword arguments:
	entry -- A list object
	"""

	cfg.C.execute("DELETE FROM Contacts WHERE rowid = ?", '{}'.format(get_id(entry)))

	del_confirm = input("Are you sure you want to delete the contact? (1/0)")

	if del_confirm == '1':
		cfg.DB.commit()


def edit_entry(entry):
	"""Updates entry in database.

	Keyword arguments:
	entry -- A list object
	id -- Corresponding ID number for an entry.
	"""

	entry_update = '''UPDATE Contacts SET First = ?, Last = ?, Street1 = ?,
			Street2 = ?, City = ?, State = ?, Zip = ?, Home = ?, Mobile = ?, 
			Email = ?, Birthday = ?, Notes = ? WHERE rowid = ? '''

	cfg.C.execute(entry_update, [entry[0], entry[1], entry[2], entry[3], 
		entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10],
		entry[11], '{}'.format(get_id(entry))])

	cfg.DB.commit()


def query_entrylist(sort):
	"""Prints the full list of entries in database.

	Keyword arguments:
	sort -- String containing sorting method
	"""

	# Choose the sorting method
	if sort == 'last':
		last_name = '''SELECT * FROM Contacts ORDER BY Last'''
		cfg.C.execute(last_name)

	elif sort == 'zip':
		zip_code = '''SELECT * FROM Contacts ORDER BY Zip ASC'''
		cfg.C.execute(zip_code)

	# for row in cfg.C:
		# return row

	return cfg.C

def search_entry(str):
	"""Searches the database for an entry.

	Keyword arguments:
	str -- A string containing search term
	"""
	search = '''SELECT * FROM Contacts WHERE (First || Last || Street1 || 
			Street2 || City || State || Zip || Home || Mobile || Email || 
			Birthday || Notes) LIKE '%' || ? || '%' '''
	cfg.C.execute(search, [str]) 

	# for row in cfg.C:
	# 	return row

	return cfg.C



if __name__ == "__main__":
	entry0 = ['Travis', 'Barnes', '555-555-5555', '555-444-4444', 'ttb@uoregon.edu', 'street ad1',
				'street ad2', 'Eugene', 'OR', '11111', '08/30/1991', 'Insert notes here']

	entry1 = ['George', 'Castanza', '555-333-3333', '', 'castanza@seinfeld.com', '5th street',
				'', 'NYC', 'NY', '11111', '', '']

	entry2 = ['Giacomo', 'Ouillizzoni', '555-222-2222', '', 'gguillizzoni@mail.com', '123 Fake St.',
				'Apt 7', 'FakeTown', 'FakeState', '33333', '', 'Cool dude.']

	entry3 = ['Thomas', 'Mark', '555-777-7777', '', 'markt@mail.com', '',
				'', 'City', 'State', '33333', '', '']

	entry3_edit = ['Thomas', 'Mark', '555-777-7777', '555-000-0000', 'markt@mail.com', '',
				'', 'City', 'State', '33333', '10/13/97', '']
					
	filename = input("Enter the name of the address book file: ")
	print("Opening database...")
	db_init(filename)
	print("Database opened\n")

	print("Printing contacts...")
	for row in query_entrylist('last'):
		print(row)

	# if db_exists(filename) == False:
	print("\nInserting contacts...")
	insert_entry(entry0)
	insert_entry(entry1)
	insert_entry(entry2)
	insert_entry(entry3)
	print("Printing contacts...")
	for row in query_entrylist('last'):
		print(row)

	print("\nDeleting contact Travis... ")
	delete_entry(entry0)
	print("Printing contacts...")
	for row in query_entrylist('last'):
		print(row)

	print("\nInserting contact Travis... ")
	insert_entry(entry0)
	print("Printing contacts...")
	for row in query_entrylist('last'):
		print(row)

	print("\nSorting contacts by zip code...")
	for row in query_entrylist('zip'):
		print(row)

	print("\nEditing contact Thomas...")
	edit_entry(entry3_edit)
	print("Printing contacts...")
	for row in query_entrylist('last'):
		print(row)

	print("\nCreating new entry list...")
	entry_list = create_entry('charles', 'sanders', '1000 West St', 'Apt203', 'Townville', 'State', '131313', 
		'777-777-7777', '754-333-3333', 'email@mail.com', '01/01/1900', '')
	print(entry_list)
	print("\nInserting entry... ")
	insert_entry(entry_list)
	print("Printing contacts...")
	for row in query_entrylist('last'):
		print(row)

	print("\nDeleting entry...")
	delete_entry(entry_list)
	print("Printing contacts...")
	for row in query_entrylist('last'):
		print(row)

	print("\nSearching for zip code 111111...")
	for row in search_entry('11111'):
		print(row)

	print("\nSearching for partial email @mail.com...")
	for row in search_entry('@mail.com'):
		print(row)

	print("\nSearching for name George and george...")
	for row in search_entry('George'):
		print(row)
	for row in search_entry('george'):
		print(row)

	print("\nSearching for letter f...")
	for row in search_entry('f'):
		print(row)