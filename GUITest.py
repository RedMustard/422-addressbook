import threading
import AddressBook as ab
import gui
import tkinter as Tk

class EventGen(threading.Thread):
	def __init__(self, target):
		threading.Thread.__init__(self)
		self.target = target
	
	def run(self):
		#let gui start
		import time
		time.sleep(0.2)
		
		#force focus to widget
		self.target.focus_force();
		
		
		#generate mouse 1
		self.target.event_generate("<ButtonPress>")
		self.target.event_generate("<ButtonRelease")

		self.target.update()




if __name__ == "__main__":
	ab.new_book()
	root = Tk.Tk()
	gui.mainWindow(root)
	
	egen = EventGen(root)
	
	egen.start()
	root.mainloop()

