from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk

import socket 
import time 
import threading 

#Server 

def serverrun(clients, ser):
	print ('Server has started')
	ser.start_listening(1)
	while True:
		try: 
			data,addr = s.recv(1024).decode('utf-8')
			if 'Quit' in str(data):
				break 
			if addr not in clients: 
				clients.append(addr)

			print (time.ctime(time.time()) + str(addr) + " : :" + str(data))
			for clients in clients: 
				s.send(data.encode())
		except: 
			pass 

	ser.close()

host = '127.0.0.1'
print ('HOST: ',host)
port = 5000
clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

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

			def serverrun(clients, ser):
				print ('Server has started')
				ser.start_listening(1)
				while True:
					try: 
						data,addr = s.recv(1024).decode('utf-8')
						if 'Quit' in str(data):
							break 
						if addr not in clients: 
							clients.append(addr)

						print (time.ctime(time.time()) + str(addr) + " : :" + str(data))
						for clients in clients: 
							s.send(data.encode())
					except: 
						pass 

				ser.close()

#SERVER CODE:

#BIND EVENTS 


#MOUSE event configuration 


#Keyboard bind event configuration 
root = Tk()
my_app = Imapp(root)

thr = threading.Thread(target = serverrun, args = (clients, s,))
thr.start()

root.mainloop()
thr.join()
