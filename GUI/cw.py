import tkinter as Tk
import AddressBook as ab
import gui

class ConfirmationWindow(object):
	def yes(self):
		#self.top.destroy()
		print('hello')

	def no(self):
		print('bye')
	
	def __init__(self,master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title('Confirm')

		self.label = Tk.Label(top, text = 'Are you sure you want to do this?')
		self.label.grid(row = 0, column = 1, padx = 10, pady = 10)

		self.yes_button = Tk.Button(top, text = 'Yes', command = self.yes )
		self.yes_button.grid(row = 1, column = 1, sticky = Tk.E)

		self.no_button = Tk.Button(top, text = 'No', command = self.no)
		self.no_button.grid(row = 1, column = 2)