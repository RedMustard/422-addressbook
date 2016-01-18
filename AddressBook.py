"""
author: austin gheen
CIS422 Winter 2016

AddressBook.py
"""
import tkinter as Tk
import main as m

#  Need a function that initializes a new database upon application opening. i.e. when you
# 		input the name of the database, a call is made to add any existing entries into book_list
#  Check out item_return to see how the call is made to get_contacts()

class mainWindow(object):

    def item_return(self):
        r = self.item.get()
        m.add_contact(r)
        self.book_list.delete(0, Tk.END)
        for contact in m.get_contacts('last'):
            self.book_list.insert(Tk.END, contact)

    def popup(self):
        self.w=AddContactWindow(self.master)
        self.master.wait_window(self.w.top)

    def __init__(self,master):
        self.master = master
        master.title('Address Book')
        self.item = Tk.Entry(master)
        self.item.grid(row=2, column = 1, pady = 10)
        self.item.insert(0, 'Enter name')
        self.submit = Tk.Button(master, text='Submit', command = self.item_return)
        self.submit.grid(row = 3, column = 1)
        self.scrollbar = Tk.Scrollbar(master)
        self.scrollbar.grid(row = 4, column = 2)
        self.book_list = Tk.Listbox(master, yscrollcommand = self.scrollbar.set)
        self.book_list.grid(row = 4, column = 1, padx = 10, pady = 10, columnspan= 3)
        self.scrollbar.config(command = self.book_list.yview)
        self.add_button = Tk.Button(master, text = 'Add', command = self.popup)
        self.add_button.grid(row= 5, column = 2)
        #ADD THE ADD BUTTON


class AddContactWindow(object):

    def __init__(self,master):
        top=self.top=Tk.Toplevel(master)
        self.master = master
        master.title('Add Contact')

        self.first_name_label = Tk.Label(top, text = 'First Name:')
        self.first_name_label.grid()

        #input for contacts first name
        self.first_name = Tk.Entry(top)
        self.first_name.grid(row = 0, column = 1)

        self.last_name_label = Tk.Label(top, text = 'Last Name:')
        self.last_name_label.grid(row = 1) 

        #input for contacts last name
        self.last_name = Tk.Entry(top)
        self.last_name.grid(row = 1, column = 1)

        self.address1_label = Tk.Label(top, text = 'Address 1:')
        self.address1_label.grid(row = 2)

        #input for contacts address1
        self.address1 = Tk.Entry(top)
        self.address1.grid(row = 2, column = 1)

        self.adress2_label = Tk.Label(top, text = 'Address 2:')
        self.adress2_label.grid(row = 3)

        #input for contacts address2
        self.address2 = Tk.Entry(top)
        self.address2.grid(row = 3, column = 1)

        self.email_label = Tk.Label(top, text = 'e-Mail:')
        self.email_label.grid(row = 4)

        #input for contacts email
        self.email = Tk.Entry(top)
        self.email.grid(row = 4, column = 1)

        self.birthday_label = Tk.Label(top, text = 'Birthday:')
        self.birthday_label.grid(row = 5)

        #input for contacts birthday
        self.birthday = Tk.Entry(top)
        self.birthday.grid(row = 5, column = 1)

        self.notes_label = Tk.Label(top, text = "Notes")
        self.notes_label.grid(row = 6)

        #input for notes on contact
        self.notes = Tk.Entry(top)
        self.notes.grid(row = 6, column = 1)

        self.cancel_button = Tk.Button(top, text = 'Cancel')#NEED TO MAKE BUTTON FUNCTIONAL
        self.cancel_button.grid(row = 8, column = 2)

        self.add_button = Tk.Button(top, text= 'Add')#NEED TO MAKE BUTTON FUNCTIONAL
        self.add_button.grid(row = 7, column = 2)



if __name__ == "__main__":
    master = Tk.Tk()
    m=mainWindow(master)
    w=AddContactWindow(master)
    master.mainloop()