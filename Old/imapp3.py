from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk

import socket 
import time 
import threading 
import _thread

#Server 

#GUI CODE 
class Imapp: 


	def __init__(self, master): 

			master.title("Jimmy's Instant Messaging App")
			master.geometry('400x400+900+500')
			master.resizable(False, False)

#SERVER CODE:

#WIDGET CREATION 
			
			self.top_frame = Frame(master)
			self.top_frame.pack()

			self.toppanel = Canvas(self.top_frame, background='black', height=50, width=400)
			self.toppanel.pack()

			self.bimage = ImageTk.PhotoImage(Image.open('rsettings.png').resize((25,25)))
			self.toppanel.create_image(370,30, image = self.bimage)

			self.middle_frame = Frame(master)
			self.middle_frame.pack() 

			self.canvas = Canvas(self.middle_frame, background='black', height=300, width=400)
			self.canvas.pack()

			self.bottom_frame = Frame(master, background='white')
			self.bottom_frame.pack()

			self.username = Label(self.bottom_frame, width = 10, text = 'Username', background='black', fg='yellow', font=('Arial',14))
			self.username.grid(row=0,column=0)

			self.entry = Entry(self.bottom_frame, width = 20)
			self.entry.grid(row=0,column=1)

			self.send_button = ttk.Button(self.bottom_frame, text = 'Send')
			self.send_button.grid(row=0,column=2)

#SERVER CODE:

def GUIrun(root): 
	root.mainloop()

def change_username(string, root):
	root.username.configure(text = string)

#BIND EVENTS 

def serverrun(clients, ser,root):
	print ('Server has started')
	ser.start_listening(3)
	conn, addr = ser.accept()
	print('Establishing connection with: ', addr)

	conn.send(str.encode('Enter a username: '))
	global username
	user = conn.recv(1024).decode('utf-8')
	change_username(user, root)

	while True:
		print ("Clients: ", clients)
		data = conn.recv(1024).decode('utf-8')
		print ('s')
		if 'Quit' in str(data):
			break 
		if 'Finish' in str(data): 
			print('Shutting Down.....\nPlease Wait a Moment')
			ser.close()
			root.quit()
			exit()
		if str(addr[1]) not in clients: 
			clients.append(str(addr[1]))
		print (time.ctime(time.time()) + str(addr) + " : :" + str(data.encode()))
		for client in clients: 
			conn.send(str.encode(data))
	ser.close()


#MOUSE event configuration 
#SERVER CODE:
host = '127.0.0.1'
print ('HOST: ',host)
port = int(input("Select a port: "))
clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('INFO: ' + host + ':' + str(port))
s.bind((host,port))

#Keyboard bind event configuration 
global root
root = Tk()
my_app = Imapp(root)

_thread.start_new_thread(serverrun, (clients, s,root,))

root.mainloop()



