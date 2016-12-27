import threading 
from tkinter import *
import time

cLock, rLock = threading.Lock(),threading.Lock()

def exiting():
	root.destroy()

def threads():
	time.sleep(3)
	print('Finished')

	while True:	
		cLock.acquire()
		if my_app.button_pressed: 
			sendm = my_app.entry.get()
			my_app.entry.delete(0,END)
			themessage = username + " :: " + sendm
			if sendm != '':
				ser.send(str.encode(themessage))
				print ('Just sent: ', sendm)
			print ('Button pressed: ', my_app.button_pressed)
			my_app.button_pressed = False
		cLock.release()
		time.sleep(0.5) 

root = Tk()

t1 = threading.Thread(target = threads)
t2 = threading.Thread(target = threads)
t1.start()
t2.start()

root.mainloop()
print('Joining')
#t1.join()
#t2.join() 

