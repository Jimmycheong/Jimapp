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
clientsd ={}
connexs = []

#===##===##===##===##===##===##===##===#
#BROADCAST
#===##===##===##===##===##===##===##===#

#def senddata(data, source):
def senddata(conn,data, source):
	print ('<===SENDING===>')
	print('Source: ', source)
	for connex in connexs: 
		print ('Current connex: ',connex.getpeername()) 
		themess = source + "::" + data
		conn.sendto(str.encode(themess),connex.getpeername())
	print ('<===COMPLETE===>')

#===##===##===##===##===##===##===##===#
#INDIVIDUAL THREAD OPERATION
#===##===##===##===##===##===##===##===#

def serverrun(conn, loop):
	print ('#==============#')
	print ('Server has started')
	print('Current Thread: ', threading.current_thread())
	usersname=conn.recv(1024).decode('utf-8')
	print ('Username added: ', usersname)
	joiner = conn.getpeername()
	if joiner not in clientsd:
		clientsd[joiner] = usersname
	print ('Clients:', clients)
	print ('#==============#')
	while True:
		data = conn.recv(1024).decode('utf-8')
		first,seccond = data.split('::')
		print('Received data: from {}'.format(first) + '\nAt '+ time.ctime(time.time()) + ':: ', second)
		if 'Quit' in str(second):
			break 
		if 'Finish' in str(data): 
			print('Shutting Down.....\nPlease Wait a Moment')
			s.close()
			break
		senddata(conn,data, source)
	s.close()

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
	connexs.append(conn)
	#Threading and Looping
	nT = threading.Thread(target = serverrun, args =(conn, Loop)) 
	nT.daemon =True
	nT.start() 

