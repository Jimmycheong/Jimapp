import socket 
import time 
from _thread import *
import sys
import threading

#===##===##===##===##===##===##===##===#
#SERVER INFO
#===##===##===##===##===##===##===##===#

host = '127.0.0.1'
print ('HOST: ',host)
port = 5552
port = int(input("Select a port: "))
global clients
clients = []
connexs = []
usernames = []

#===##===##===##===##===##===##===##===#
#BROADCAST
#===##===##===##===##===##===##===##===#

#def senddata(data, source):
def senddata(data, source):
	for connex in connexs:
		print ('Current client: ', connex.getpeername())
#		connex.sendto(source.encode(),connex.getpeername())

		connex.sendto(data.encode(),connex.getpeername())

#===##===##===##===##===##===##===##===#
#INDIVIDUAL THREAD OPERATION
#===##===##===##===##===##===##===##===#

def serverrun(conn, loop):
	print ('Server has started')
	print('Current Thread: ', threading.current_thread())

	while True:
		data = conn.recv(1024).decode('utf-8')
		print('Received data', data)
		if 'Quit' in str(data):
			break 
		if 'Finish' in str(data): 
			print('Shutting Down.....\nPlease Wait a Moment')
			s.close()
			break
		print (time.ctime(time.time()) + str(addr) + " : :" + str(data.encode()))
#		senddata(data, source)
		source = conn.getpeername()
		senddata(data, source)
	s.close()
	rejoin(threading.current_thread())

def rejoin(inthread):
	inthread.join()


#===##===##===##===##===##===##===##===#
#SERVER GO CODE
#===##===##===##===##===##===##===##===#

global s
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('INFO: ' + host + ':' + str(port))
s.bind((host,port))

s.listen(3)
print ('Waiting for connection.....')

Loop = True 

while Loop: 
	conn, addr = s.accept()
	print('Establishing connection with: ', conn.getpeername())

	usersname=conn.recv(1024).decode('utf-8')
	print ('Username added: ', usersname)
	if usersname not in clients: 
		clients.append(usersname)
		#clients[usersname] = conn.getpeername()
		connexs.append(conn)

		print ('Clients:', clients)
	#Threading and Looping
		global nT
		nT = threading.Thread(target = serverrun, args =(conn, Loop)) 
		nT.daemon =True
		nT.start() 
	conn.close()





