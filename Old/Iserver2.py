import socket 
import time 
from _thread import *
import sys
import threading
import argparse

#===##===##===##===##===##===##===##===#
#SERVER INFO
#===##===##===##===##===##===##===##===#

def Main(host,port):

	print('#=================#\nServer has started\n')
	print ('Hosting on: ' + host + ':' + str(port) + '\n#=================#')
	clients, connexs ={}, [] 

	#===##===##===##===##===##===##===##===#
	#BROADCAST
	#===##===##===##===##===##===##===##===#

	def senddata(data):
		print ('<===SENDING===>')
		for connex in connexs: 
			print ('Current connex: ',connex) 
			for dclient in clients: 
				if dclient == connex.getpeername():
					connex.sendto(str.encode(data),dclient)
		print ('<===COMPLETE===>')

	#===##===##===##===##===##===##===##===#
	#INDIVIDUAL THREAD OPERATION
	#===##===##===##===##===##===##===##===#

	def serving_thread(conn, loop):
		print ('#==============#')
		print('New Thread: ', threading.current_thread())
		print ('Connection established')
		usersname=conn.recv(1024).decode('utf-8')
		print ('Username added: ', usersname)
		joiner = conn.getpeername()
		if joiner not in clients:
			clients[joiner] = usersname
		print ('Clients:', clients)
		print ('#==============#')
		while True:
			data = conn.recv(1024).decode('utf-8')
			splat = data.split('::')
			print('Received data: from {}'.format(splat[0]) + '\nAt '+ time.ctime(time.time()) + ':: ', splat[1])
			if 'Quit' in str(splat[1]):
				break 
			if 'Finish' in str(splat[1]): 
				print('Shutting Down.....\nPlease Wait a Moment')
				s.close()
				break
			senddata(data)
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

		#Generating and starting new thread
		nT = threading.Thread(target = serving_thread, args =(conn, Loop)) 
		nT.daemon =True
		nT.start() 

#===##===##===##===##===##===##===##===#
#Terminal run code 
#===##===##===##===##===##===##===##===#

if __name__ == '__main__': 
	parser = argparse.ArgumentParser()
	parser.add_argument("--p", help = "Port number")
	parser.add_argument("--a", help = "Address number")
	args = parser.parse_args()

	try: 
		port = int(args.p)
	except:
		port = 5000 
	try: 
		address = str(args.a)
	except:
		address = '127.0.0.1' 

	Main(address,port) 

