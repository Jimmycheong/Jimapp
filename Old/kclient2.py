from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk

import socket 
import time 
from _thread import *

#WIDGET CREATION 
#===##===##===##===##===##===##===##===#
#GUI CODE 
#===##===##===##===##===##===##===##===#
global master
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

def GUIrun(root): 
	root.mainloop()

def change_username(string):
	username.configure(text = string)

def connector(ser,root, username, server):
	print('Established connection with: ', server)
#
	ser.send(str.encode(usersname))
	while True:				
		message = input('--> ')	
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

#Personal info:
host = '127.0.0.1'
port = 0 
server = ('127.0.0.1', 5558)

usersname = input('Enter a username:') 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

#Threading and Looping
start_new_thread(connector, (s,master,usersname, server))
master.mainloop() 
