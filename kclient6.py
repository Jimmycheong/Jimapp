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
					global store_user
					global store_address
					store_user = self.ientryuser.get() 
					store_address = self.ientryserver.get()
					print ('Entered Username: ', store_user) 
					print ('Entered Address: ', store_address)	
					auth(my_app, store_user)		

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

		self.username = Label(self.bottom_frame, width = 10, text = 'username', background='white', fg='black', font=('Arial',14))
		self.username.grid(row=0,column=0)

		self.entry= Entry(self.bottom_frame, width = 20)
		self.entry.grid(row=0,column=1)

		self.send_button = ttk.Button(self.bottom_frame, text = 'Send', command = lambda :send_entry())
		self.send_button.grid(row=0,column=2)

		global inserting
		inserting = False

		def send_entry(): 
			inserting = self.entry.get() 
			#self.texts.insert('1.0' , '\n {}: '.format(username) + str(inserting))

		def send_entrykey(event):
			send_entry()

		master.bind('<Return>', send_entrykey)

def GUIrun(root): 
	root.mainloop()

def change_username(string):
	username.configure(text = string)

#def emessage():
#	fmessage = input('--> ')


def connector(ser,root,username):	
	print('Established connection with: ', server)
	ser.send(str.encode(username))
	while True:				
		print ('Passed starter')
		while not inserting: 
			time.sleep(3)
			print('ON standby.. ')
		ser.send(str.encode(inserting))
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
	shutdown = True
	cT.join()
	rT.join()
	ser.close()

def receiver(sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                rdata, raddr = sock.recvfrom(1024)
                print (str(rdata))
        except:
            pass
        finally:
            tLock.release()

#===##===##===##===##===##===##===##===#

global root
root = Tk()
global my_app
my_app = Initial(root)

input_username = "default"
input_address = "127.0.0.01" 
shutdown = False
tLock = threading.Lock()

def create_threads(s,username): 
	global cT, rT
	cT = threading.Thread(target = connector, args = (s,root,username))
	cT.start()
	rT = threading.Thread(target = receiver, args = (s,))
	rT.start()

def socket_creation(username): 
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(server) 

	#Threading and Looping
	create_threads(s,username)


def auth(my_app, store_username):
	my_app.icanvas.pack_forget()
	my_app = MainP(root)
	my_app.username.configure(text=store_username) 
	print ("Completed 1st section")
	socket_creation(store_username)  

#Personal info:
host = '127.0.0.1'
port = 0 
server = ('127.0.0.1', 5555)


root.mainloop() 
