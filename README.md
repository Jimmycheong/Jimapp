# Jimapp - Instant Messaging Application 

- My second Python app! 
- Consists of two elements : server and client
- Uses the Tkinter module for GUI development 
- Time taken to build version 1: 2 days 
- Requires installation of following Python modules: tkinter, pillow 

# Main Graphical User Interface
![screen shot 2016-12-30 at 16 41 48](https://cloud.githubusercontent.com/assets/22529514/21568752/f48598aa-ceae-11e6-8959-2a271a2d8f58.jpg)

# How does it work? 
- The server listens for all incoming messages and broadcasts them to all connected clients. 
- Multithreading of the server: The server creates new threads to handle new connecting clients. 
- Multithreading of the client: 3 threads. One to keep the GUI looping, one to listen to all incoming messages, one to send messages.   

To connect to the server, the user inputs their username, along with the IP and the port of the hosting server. 

#Initial Connect Screen: 
![screen shot 2016-12-26 at 03 42 09](https://cloud.githubusercontent.com/assets/22529514/21475113/3177bd62-cb1f-11e6-8544-93cc7be9ccc7.jpg)

# What I learnt from this project 
- How to use bind sockets to create connections (using the Socket module)
- How to build a program that runs multiple tasks (using the multithreading module) 
- Awareness of variable scope during data sharing. 
- How to specify postional/optional arguments when running script at command line (using the argparse)
- How to use the build structure code using the if __name__ == '__main__' notation. 

#Future tasks: 
- Allow the screen to automatically scroll when new messages come in. 
- Make the screen readonly so clients cannot type into the Textbox. 
- Allow users to send pictures. 
- Create user avatar 
- Make the connection process a lot easier. Perhaps by routing the server to a free IP address. 
- Build editable options for the options icon. 
