import tkinter as Tk
import db
import gui

class New_AddBookWindow(object):

	#function for when Ok button is pressed
	def ok(self):
		book_name = self.book_name.get()
		db.db_init(book_name) ## <----- PASS USER INPUT   book_name
		root = Tk.Tk()
		self.master.withdraw()
		root.protocol("WM_DELETE_WINDOW", exit)
		gui.mainWindow(root)
		root.mainloop()
		sys.exit()


	def exit():
		root.destroy()

	def close_window(self):
		self.master.destroy()


	def __init__(self, master):
		self.new = master
		self.master = master
		self.master.title('New Address Book')

		self.instruction_message = Tk.Label(self.master, text = 'Please enter the name of\n your new address book')
		self.instruction_message.grid()

		self.book_name_label = Tk.Label(self.master, text = 'Address Book Name:')
		self.book_name_label.grid(row = 1)

		#entry is for user's desired Address Book Name
		self.book_name = Tk.Entry(self.master)
		self.book_name.grid(row = 1 , column = 1, padx = 10, pady = 10)

		self.cancel_button = Tk.Button(self.master, text = 'Cancel', command = self.close_window )
		self.cancel_button.grid(row = 2, column = 2)

		self.ok_button = Tk.Button(self.master, text= 'Ok', command = self.ok )
		self.ok_button.grid(row = 2, column = 3)