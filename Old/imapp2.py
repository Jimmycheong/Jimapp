from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk

import socket 
import time 
import threading 

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

#BIND EVENTS 

def serverrun(clients, ser):
	print ('Server has started')
	ser.start_listening(1)
	conn, addr = ser.accept()
	print('connection established from: ', addr)
	setting = True 

	while setting:
		print ("Clients: ", clients)
#		try: 
		data = conn.recv(1024).decode('utf-8')
		print ('s')
		if 'Quit' in str(data):
			break 
		if 'Finish' in str(data): 
			thr.join()
			exit()
		if str(addr[1]) not in clients: 
			clients.append(str(addr[1]))
		print (time.ctime(time.time()) + str(addr) + " : :" + str(data.encode()))
		for client in clients: 
			conn.send(str.encode(data))
#		except:
#			print ("Reached") 
#			pass 
	ser.close()


#MOUSE event configuration 
#SERVER CODE:
host = '127.0.0.1'
print ('HOST: ',host)
port = 5000
clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('INFO: ' + host + ':' + str(port))
s.bind((host,port))

#Keyboard bind event configuration 
root = Tk()
my_app = Imapp(root)

thr = threading.Thread(target = serverrun, args = (clients, s,))
#thr2 = threading.Thread(target = GUIrun, args=(root,))

thr.start()
#thr2.start() 
root.mainloop()
thr.join()
#thr2.join()
