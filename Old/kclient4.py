from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk

import socket 
import time 
from _thread import *
import sys

#WIDGET CREATION 
#===##===##===##===##===##===##===##===#
#GUI CODE 
#===##===##===##===##===##===##===##===#

class Initial: 


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

			self.ibuttonserver.config(command = lambda: get_info()) 

			def get_info():
				if len(self.ientryuser.get()) > 0 and len(self.ientryserver.get()) > 0: 
					self.store_user = self.ientryuser.get() 
					self.store_address = self.ientryserver.get()
					print (self.store_user) 
					print (self.store_address)	
					auth(my_app, starter)		

class MainP: 

	def __init__(self, master): 

		master.title("Jimmy's Instant Messaging App")
		master.geometry('400x400+200+200')
		master.resizable(False, False)

		top_frame = Frame(master)
		top_frame.pack()

		toppanel = Canvas(top_frame, background='black', height=50, width=400)
		toppanel.pack()

		bimage = ImageTk.PhotoImage(Image.open('rsettings.png').resize((25,25)))
		toppanel.create_image(370,30, image = bimage)

		middle_frame = Frame(master)
		middle_frame.pack() 

		canvas = Canvas(middle_frame, background='black', height=300, width=400)
		canvas.pack()

		bottom_frame = Frame(master, background='white')
		bottom_frame.pack()

		username = Label(bottom_frame, width = 10, text = 'Username', background='black', fg='yellow', font=('Arial',14))
		username.grid(row=0,column=0)

		entry = Entry(bottom_frame, width = 20)
		entry.grid(row=0,column=1)

		send_button = ttk.Button(bottom_frame, text = 'Send')
		send_button.grid(row=0,column=2)

def GUIrun(root): 
	root.mainloop()

def change_username(string):
	username.configure(text = string)




def connector(ser,root):	
	print('Established connection with: ', server)
#
	ser.send(str.encode(usersname))
	while True:				
		print ('Passed starter')
		message = emessage()
		ser.send(str.encode(message))
		data = ser.recv(1024).decode('utf-8')
		if 'Quit' in str(data):
			break 
#		if 'Finish' in str(data): 
#			print('Shutting Down.....\nPlease Wait a Moment')
#			ser.close()
#			root.quit()
#			exit()
#		print (time.ctime(time.time()) + str(addr) + " : :" + str(data.encode()))#
#		for client in clients: 
#			conn.send(str.encode(data))
	ser.close()
	
#===##===##===##===##===##===##===##===#

root = Tk()
global my_app
my_app = Initial(root)

input_username = "default"
input_address = "127.0.0.01" 
global starter
starter = False 

def auth(my_app, starter):
#	ans = input('Ready?\n')
#	if ans == 'Yes':
	my_app.icanvas.pack_forget()
	my_app = MainP(root)
	starter = True 

#Personal info:
host = '127.0.0.1'
port = 0 
server = ('127.0.0.1', 5555)

while starter: 
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(server) 

#Threading and Looping
	start_new_thread(connector, (s,root))
root.mainloop() 
