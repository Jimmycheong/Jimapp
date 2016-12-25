from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk

class MyCalculator: 


	def __init__(self, master): 

			master.title("Jimmy's Instant Messaging App")
			master.geometry('400x400+200+200')
			master.resizable(False, False)

			self.icanvas = Canvas(master, bg = 'black')
			self.icanvas.pack(fill = BOTH, expand = True)

			self.ilabeluser = Label(self.icanvas, text = 'Username', bg ='black', fg = 'white', font = ('Arial',15, 'bold'))
			self.ilabelserver = Label(self.icanvas, text = 'Server Address', bg ='black', fg = 'white', font = ('MS Serif',15, 'bold'))
			self.ientryuser = Entry(self.icanvas, width = 20)
			self.ientryserver = Entry(self.icanvas, width = 20)
			self.ibuttonserver = ttk.Button(self.icanvas, text='Connect')

			#Geometry Manager
			self.ilabeluser.place(relx = 0.5, rely = 0.5, anchor = CENTER, y=-100 )
			self.ientryuser.place(relx = 0.5, rely = 0.5, anchor = CENTER, y= -50)
			self.ilabelserver.place(relx = 0.5, rely = 0.5, anchor = CENTER, y= 0)
			self.ientryserver.place(relx = 0.5, rely = 0.5, anchor = CENTER, y= 50)
			self.ibuttonserver.place(relx = 0.5, rely = 0.5, anchor = CENTER, y= 110)




root = Tk()
my_calculator = MyCalculator(root)

ans = input('Ready?\n')
if ans == 'Yes':
	my_calculator.icanvas.pack_forget()

root.mainloop() 