"""
Test cases for Addressbook

Author: James Dolan

TODO:

verify sorting is succesful
verify search is succesful
"""

import sys, os
from db import *

def main():
        entry0 = ['Travis', 'Barnes', 'street ad1', 'street ad2', 'Eugene', 'OR', '11111',
                                '555-555-5555', '555-444-4444', 'ttb@uoregon.edu', '08/30/1991',
                                'Insert notes here']

        entry1 = ['George', 'Castanza', '5th street','', 'NYC', 'NY', '11111',
                                '555-333-3333', '', 'castanza@seinfeld.com', '' , '']

        entry2 = ['Giacomo', 'Ouillizzoni', '123 Fake St.','Apt 7', 'FakeTown', 'FakeState',
                                '33333','555-222-2222', '', 'gguillizzoni@mail.com',  '', 'Cool dude.']

        entry3 = ['Thomas', 'Mark',  '', '', 'City', 'State', '33333','555-777-7777',
                                '', 'markt@mail.com', '', '']

        entry3_edit = ['Lucy', 'Mark', '', '', 'City', 'State', '33333','555-777-7777',
                                '555-000-0000', 'markt@mail.com',  '10/13/97', '']

        
        'testing connection to db'
        print("### connecting to db ###")

        try:
                os.system('rm Test.ab')
                db_init("Test")
                if(db_exists("Test")):
                        print("*** connected succesfully ***")
                else:
                        raise Exception
        except:
                print('!!! connection failed !!!')
        
        'testing insertion'
        print('\n### testing insertion ###')
        try:
                insert_entry(entry0)
                insert_entry(entry1)
                insert_entry(entry2)
                insert_entry(entry3)
                if(get_id(entry0) and get_id(entry1) and get_id(entry2) and get_id(entry3)):
                        print('*** inserted entries succesfully ***')
                else:
                        raise Exception
        except:
                print('!!! insertion failed !!!')

        'testing deletion'
        print('\n### testing deletion ###')
        try:
                delete_entry(entry0)
                if(not get_id(entry0)):
                        print('*** delete succesful ***')
                else:
                        raise Exception
        except:
                print('!!! deletion failed !!!')


        'testing search'
        print('\n### testing search ###')
        try:
                search_entry('Travis')
                print('*** search successful ***')
        except:
                print('!!! search failed !!!')


        'testing sorting'
        print('\n### testing sorting ###')
        try:
                query_entrylist('zip')
                query_entrylist('last')
                print('*** sorting succesful ***')
        except:
                print('!!! sorting failed !!!')

        'testing editing'
        print('\n### testing sorting ###')
        try:
                edit_entry(entry3_edit)
                if(search_entry('Lucy')):
                        print('*** edit succesful ***')
                else:
                        raise Exception
        except:
                print('!!! edit failed !!!')



        
        
        os.system('rm Test.ab')
        os.system('rm __pycache__/config.cpython-34.pyc')
        os.system('rm __pycache__/db.cpython-34.pyc')


if __name__ == "__main__":
        main()
        