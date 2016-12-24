from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk

import socket 
import time 
import threading 

#WIDGET CREATION 
#===##===##===##===##===##===##===##===#
#GUI CODE 
#===##===##===##===##===##===##===##===#
master = Tk()
master.title("Jimmy's Instant Messaging App")
master.geometry('400x400+900+500')
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

def serverrun(clients, ser):
	print ('Server has started')
	ser.listen(1)
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
	
#===##===##===##===##===##===##===##===#

#SERVER CODE:
host = '127.0.0.1'
print ('HOST: ',host)
port = 5000
clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('INFO: ' + host + ':' + str(port))
s.bind((host,port))

#Threading 
global thr
thr = threading.Thread(target=serverrun, args=(clients,s,))

thr.start()

#SERVER CODE:


#BIND EVENTS 


#MOUSE event configuration 


#Keyboard bind event configuration 
master.mainloop() 

thr.join() 