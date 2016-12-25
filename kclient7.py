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

#MAIN PROGRAM

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

		self.send_button = ttk.Button(self.bottom_frame, text = 'Send', command = lambda :self.send_entry())
		self.send_button.grid(row=0,column=2)

		def send_entrykey(event):
			send_entry()
		
		master.bind('<Return>', send_entrykey)

		#global inserting
		#inserting = ""
		#inserting = False	

	def send_entry(self): 
		button_pressed = True
#		insert = self.entry.get()
#		self.entry.delete(0,END)

		#self.texts.insert('1.0' , '\n {}: '.format(username) + str(inserting))



def GUIrun(root): 
	root.mainloop()

def change_username(string):
	username.configure(text = string)

#def emessage():
#	fmessage = input('--> ')


#===##===##===##===##===##===##===##===#
#THREAD ONE - SENDER
#===##===##===##===##===##===##===##===#
def connector(ser,my_app,username,c_shutdown):	
	global button_pressed
	button_pressed = False
	print('Established connection with: ', server)
	ser.send(str.encode(username))
	print ('Username entered')
	while not c_shutdown:	
		print ('Waiting...')
		cLock.acquire()
		if button_pressed: 
			sendm = my_app.entry.get()
			if sendm != '':
				print ('Just sent: ', sendm)
		#if sendm != "": 
		#	ser.send(str.encode(inserting))
		#	print('Sending: ', inserting)
		cLock.release()
		time.sleep(0.5) #Buffer

	r_shutdown = True
	c_shutdown =True
	cT.join()
	rT.join()
	ser.close()      

#===##===##===##===##===##===##===##===#
#THREAD TWO - RECEIVER
#===##===##===##===##===##===##===##===#

def receiver(sock, r_shutdown):
	while not r_shutdown:
	  try:
	  	rLock.acquire()
	  	while True:
	  		rdata, raddr = sock.recvfrom(1024)
	  		print (str(rdata.decode('utf-8')))
	  except:
	  	pass
	  finally:
	  	rLock.release()
	r_shutdown = True
	c_shutdown =True
	cT.join()
	rT.join()
	ser.close()           

#===##===##===##===##===##===##===##===#

global root, my_app,c_shutdown, r_shutdown
root = Tk()
my_app = MainP(root)
#print ('Exists:', my_app.send_entry())
my_app.top_frame.pack_forget()
my_app.texts.pack_forget()
my_app.bottom_frame.pack_forget()

input_username = "default"
input_address = "127.0.0.01" 
c_shutdown,r_shutdown = False, False
cLock,rLock = threading.Lock(),threading.Lock()


def create_threads(s,username): 
	global cT, rT
	cT = threading.Thread(target = connector, args = (s,my_app,username,c_shutdown,))
	rT = threading.Thread(target = receiver, args = (s,r_shutdown))
	cT.start()
	print ("Connecting thread: started") 
	rT.start()
	print ("Receiving thread: started") 

def socket_creation(username): 
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(server) 

	#Threading and Looping
	create_threads(s,username)


def auth(my_app, store_username):
	my_app.icanvas.pack_forget()
	my_app.username.configure(text=store_username) 
	print ("Completed 1st section")
	socket_creation(store_username)
	my_app.top_frame.pack()
	my_app.texts.pack()
	my_app.bottom_frame.pack()


#Personal info:
host = '127.0.0.1'
port = 0 
server = ('127.0.0.1', 5553)


root.mainloop() 
