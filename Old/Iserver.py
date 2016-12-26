import socket 
import time 
from _thread import *
import sys
import threading
import argparse

#===##===##===##===##===##===##===##===#
#SERVER INFO
#===##===##===##===##===##===##===##===#

def Main(port):

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

	def senddata(data):
		print ('<===SENDING===>')
		for connex in connexs: 
			print ('Current connex: ',connex) 
			for dclient in clientsd: 
				if dclient == connex.getpeername():
					connex.sendto(str.encode(data),dclient)
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
		print ('Clientsd:', clientsd)
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
		#Threading and Looping
		nT = threading.Thread(target = serverrun, args =(conn, Loop)) 
		nT.daemon =True
		nT.start() 

if __name__ == '__main__': 
	parser = argparse.ArgumentParser()
	try: 
		port = parser.add_argument("--p", help = "Port number")
		print ("Host port: " ,parser.parse_args().p)
	except:
		port = 5000 

	Main(port) 

