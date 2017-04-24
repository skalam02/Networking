#Stylianos Kalamaras
#Project 1
#CSCI 379 Networking
#Professor Jie Chu
#03/10/17

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname()  #Get local machine name
port = 9999               # Reserve a port for your service.

s.connect((host, port))
sentence = raw_input("Enter a sentence: ")
s.send(sentence)
response = s.recv(1024)
print (response)
command = raw_input("")
command =command.lower()
if (command != "upper" and command!= "lower"):
	command = "reverse"
s.send(command)
modified_sentence = s.recv(1024)
print("Running function "+ command+": "+ modified_sentence)
s.close()                     # Close the socket when done
