#client for simple ssl connection

import socket
import ssl

HOST = "127.0.0.1"
PORT = 7002
MAX_PACKET_SIZE = 64

#getting host addrinfo
HOST = socket.getaddrinfo(HOST, PORT)[0][4][0]
print ("HOST = " + HOST)


#Create socket
print("Connecting to host " + HOST + " on port " + str(PORT))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
##NEED TO WORK ON THIS ERROR CATCH
if sock:
	print("Connection to host " + HOST + " on port " + str(PORT) + " was successful")
else:
	print("something went wrong...")
	sock.close()

#main execution
try:
	
	#sending data
	message = 'this is the data to be sent'
	print("Message = " + message)
	sock.sendall(message)
	print("Message sent.")
	
	#wait for response
	a_received = 0
	a_expected = len(message)
	
	while a_received < a_expected:
		data =sock.recv(MAX_PACKET_SIZE)
		a_received += len(data)
		print("received " + data)
finally:
	print("Closing socket...")
	sock.close()
	##NEED ERROR CATCH HERE
	print("Socket closed successfully.")
