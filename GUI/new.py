import tkinter as Tk

class New_AddBookWindow(object):

	#function for when Ok button is pressed
	def ok(self):
		print('Ok')

	def close_window(self):
		self.top.destroy()

	def __init__(self, master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title('New Address Book')

		self.instruction_message = Tk.Label(top, text = 'Please enter the name of\n your new address book')
		self.instruction_message.grid()

		self.book_name_label = Tk.Label(top, text = 'Address Book Name:')
		self.book_name_label.grid(row = 1)

		#entry is for user's desired Address Book Name
		self.book_name = Tk.Entry(top)
		self.book_name.grid(row = 1 , column = 1, padx = 10, pady = 10)

		self.cancel_button = Tk.Button(top, text = 'Cancel', command = self.close_window )
		self.cancel_button.grid(row = 2, column = 2)

		self.ok_button = Tk.Button(top, text= 'Ok', command = self.ok )
		self.ok_button.grid(row = 2, column = 3)