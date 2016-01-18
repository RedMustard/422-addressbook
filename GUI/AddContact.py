"""
author: austin gheen
CIS422 Winter 2016

window for adding a new contact
"""
import Tkinter as Tk

root = Tk.Tk()
root.title('Add Contact')

first_name_label = Tk.Label(root, text = 'First Name:')
first_name_label.grid()

#input for contacts first name
first_name = Tk.Entry(root)
first_name.grid(row = 0, column = 1)

last_name_label = Tk.Label(root, text = 'Last Name:')
last_name_label.grid(row = 1) 

#input for contacts last name
last_name = Tk.Entry(root)
last_name.grid(row = 1, column = 1)

address1_label = Tk.Label(root, text = 'Address 1:')
address1_label.grid(row = 2)

#input for contacts address1
address1 = Tk.Entry(root)
address1.grid(row = 2, column = 1)

adress2_label = Tk.Label(root, text = 'Address 2:')
adress2_label.grid(row = 3)

#input for contacts address2
address2 = Tk.Entry(root)
address2.grid(row = 3, column = 1)

email_label = Tk.Label(root, text = 'e-Mail:')
email_label.grid(row = 4)

#input for contacts email
email = Tk.Entry(root)
email.grid(row = 4, column = 1)

birthday_label = Tk.Label(root, text = 'Birthday:')
birthday_label.grid(row = 5)

#input for contacts birthday
birthday = Tk.Entry(root)
birthday.grid(row = 5, column = 1)

notes_label = Tk.Label(root, text = "Notes")
notes_label.grid(row = 6)

#input for notes on contact
notes = Tk.Entry(root)
notes.grid(row = 6, column = 1)

cancel_button = Tk.Button(root, text = 'Cancel')#NEED TO MAKE BUTTON FUNCTIONAL
cancel_button.grid(row = 8, column = 2)

add_button = Tk.Button(root, text= 'Add')#NEED TO MAKE BUTTON FUNCTIONAL
add_button.grid(row = 7, column = 2)

if __name__ == "__main__":
	root.mainloop()