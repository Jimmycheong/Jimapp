import socket 
import time 
from _thread import *
import sys

#===##===##===##===##===##===##===##===#
#SERVER INFO
#===##===##===##===##===##===##===##===#

host = '127.0.0.1'
print ('HOST: ',host)
port = 5554
#port = int(input("Select a port: "))
clients = []

def serverrun(conn, loop):
	print ('Server has started')
	Inner = True

	usersname=conn.recv(1024).decode('utf-8')
#	if usersname not in clients: 
#		clients.append(usersname)
#		clients.append(addr[1])

#	while Inner:
#		print ("Clients: ", clients)
#		data = conn.recv(1024).decode('utf-8')
#		if 'Quit' in str(data):
#			break 
#		if 'Finish' in str(data): 
#			print('Shutting Down.....\nPlease Wait a Moment')
#			s.close()
#			break
#		if str(addr[1]) not in clients: 
#			clients.append(str(addr[1]))
#		print (time.ctime(time.time()) + str(addr) + " : :" + str(data.encode()))
#		for client in clients: 
#			conn.send(str.encode(data))

	
#===##===##===##===##===##===##===##===#

#SERVER CODE:

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('INFO: ' + host + ':' + str(port))
s.bind((host,port))

s.listen(3)
print ('Waiting for connection.....')

Loop = True 

while Loop: 
	conn, addr = s.accept()
	print('Establishing connection with: ', addr)
#	print (conn)

	#Threading and Looping
	start_new_thread(serverrun, (conn,Loop))
