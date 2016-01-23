import tkinter as Tk
import AddressBook as ab
import gui
import db

class ConfirmationWindow(object):
	def yes(self):
		db.save_changes()
		self.top.destroy()

	def no(self):
		gui.mainWindow(self.master).contact_list()
		self.top.destroy()

	
	def __init__(self,master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title('Confirm')

		self.label = Tk.Label(top, text = 'Are you sure you want to do this?')
		self.label.grid(row = 0, column = 1, padx = 10, pady = 10)

		self.yes_button = Tk.Button(top, text = 'Yes', command = self.yes )
		self.yes_button.grid(row = 1, column = 1)

		self.no_button = Tk.Button(top, text = 'No', command = self.no)
		self.no_button.grid(row = 2, column = 1)