#Stylianos Kalamaras
#Project 1
#CSCI 379 Networking
#Professor Jie Chu
#03/10/17

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9999                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)
print("Server is actively awaiting connections")   # Listens

while True:
   c, addr = s.accept()     # Establish connection with client.
   sentence = c.recv(1024)
   c.send("OK, what function would you like to run (upper,lower,reverse)? ")
   command = c.recv(1024)
   command = command.lower()
   if (command == "upper"):
	sentence = sentence.upper()
   elif (command == "lower"):
	sentence = sentence.lower()
   else:
	sentence = sentence[::-1]
   print ('Got connection from'), addr
   c.send(sentence)
   c.close()                # Close the connection
