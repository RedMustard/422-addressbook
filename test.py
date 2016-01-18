"""
Test cases for Addressbook

Author: James Dolan
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

        entry3_edit = ['Thomas', 'Mark', '', '', 'City', 'State', '33333','555-777-7777',
                                '555-000-0000', 'markt@mail.com',  '10/13/97', '']

        
        'testing connection to db'
        print("### connecting to db ###")

        try:
                os.system('rm Test.ab')
                db_init("Test")
                print("*** connected succesfully ***")
        except:
                print('!!! connection failed !!!')
        
        'testing insertion'
        print('\n### testing insertion ###')
        try:
                insert_entry(entry0)
                insert_entry(entry1)
                insert_entry(entry2)
                insert_entry(entry3)
                print('*** inserted entries succesfully ***')
        except:
                print('!!! insertion failed !!!')

        'testing deletion'
        print('\n### testing deletion ###')
        try:
                delete_entry(entry0)
                print('*** delete succesful ***')
        except:
                print('!!! deletion failed !!!')

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
                print('*** edit succesful ***')
        except:
                print('!!! edit failed !!!')



        
        
        os.system('rm Test.ab')


if __name__ == "__main__":
        main()
        
