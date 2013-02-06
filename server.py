#server for simple ssl connection

import socket
import ssl
import sys

#Constants
HOST = '' #symbolic
PORT = 7002
LISTEN_COUNT = 5
MAX_PACKET_SIZE = 64

print("Starting server on port " + str(PORT))

#create socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#server_sock.setblocking(0)

#bind serverct(server_address)

server_sock.bind((HOST, PORT))
#allowing x connections
server_sock.listen(LISTEN_COUNT)

#main loop

while True:
	#waiting for connectionct(server_address)

	client_addr = -1
	print("Waiting on connection...")
	connection, client_addr = server_sock.accept()
	try:
		print("Accepted client from " + str(client_addr))
		#break
	except client_addr == -1:
		print("Something went wrong...")
		break
	while True:
		round = 0
		data = connection.recv(MAX_PACKET_SIZE)
		print("Received :\n" + str(data))
		if data:
			print("Resending " + str(data) + " to client at " + str(client_addr))
			connection.sendall(data)
		else:
			print("No more data from client at " + str(client_addr))
			break
