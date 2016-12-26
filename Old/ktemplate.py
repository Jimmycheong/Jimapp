from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk
from lib2to3 import *

import socket 
import time 
from _thread import *
import sys
import threading

#WIDGET CREATION 
#===##===##===##===##===##===##===##===#
#GUI CODE 
#===##===##===##===##===##===##===##===#

class MainP: 

	def __init__(self, master): 

		master.title("Jimmy's Instant Messaging App")
		master.geometry('400x400+700+200')
	#	master.resizable(False, False)

		self.top_frame = Frame(master)
		self.top_frame.pack()

		self.toppanel = Canvas(self.top_frame, background='black', height=50, width=400)
		self.toppanel.pack()

		self.bimage = ImageTk.PhotoImage(Image.open('rsettings.png').resize((25,25)))
		self.toppanel.create_image(370,30, image = self.bimage)

#		self.middle_frame = Frame(master)
#		self.middle_frame.pack(fill=BOTH, expand =1, padx = 2, pady=2) 

		self.texts = Text(master,height=15, bg='white', borderwidth=5)
		self.texts.pack()

		self.bottom_frame = Frame(master, background='white')
		self.bottom_frame.pack()

		self.username = Label(self.bottom_frame, width = 10, text = username, background='white', fg='black', font=('Arial',14))
		self.username.grid(row=0,column=0)

		self.entry= Entry(self.bottom_frame, width = 20)
		self.entry.grid(row=0,column=1)

		self.send_button = ttk.Button(self.bottom_frame, text = 'Send', command = lambda :send_entry())
		self.send_button.grid(row=0,column=2)

		def send_entry(): 
			inserting = self.entry.get() 
			self.texts.insert('1.0' , '\n {}: '.format(username) + str(inserting))

		def send_entrykey(event):
			send_entry()

		master.bind('<Return>', send_entrykey)

global username
username = 'Billy'

root = Tk()
myapp = MainP(root)
root.mainloop() 
