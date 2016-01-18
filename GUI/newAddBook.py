"""
author: austin gheen
CIS422 Winter 2016

window for adding a new address book
	-tells user to enter a desired address book name in the empty entry field
	-ok button to confirm the desired name is correct
	-cancel button if user wants to go back to main window
"""
import Tkinter as Tk

#def cancel_command()

#def ok_command()

root = Tk.Tk()
root.title('New Address Book')

instruction_message = Tk.Label(root, text = 'Please enter the name of\n your new address book')
instruction_message.grid()

book_name_label = Tk.Label(root, text = 'Address Book Name:')
book_name_label.grid(row = 1)

#entry is for user's desired Address Book Name
book_name = Tk.Entry(root)
book_name.grid(row = 1 , column = 1, padx = 10, pady = 10)

cancel_button = Tk.Button(root, text = 'Cancel')#, command = cancel_command) #NEED TO MAKE BUTTON FUNCTIONAL
cancel_button.grid(row = 2, column = 2)

ok_button = Tk.Button(root, text= 'Ok')#, command = ok_command)#NEED TO MAKE BUTTON FUNCTIONAL
ok_button.grid(row = 2, column = 3)

if __name__ == "__main__":
	root.mainloop() 