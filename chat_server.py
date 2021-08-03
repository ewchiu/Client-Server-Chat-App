# Eric Chiu
# CS 372 Summer 2021
# Client-Server Chat Implementation

import socket
import select
import sys

            

# establishes server on specified host and port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
	print("Error - not enough arguments. IP address and port number needs to be included")
	exit()

addr = str(sys.argv[1])
port = str(sys.argv[2])    

print('Listening on ' + addr + ' port ' + str(port))
print('Welcome to the chat room! To terminate the session, type /q into the chat')

# create the server using the socket module
server.bind((addr, port))
server.listen(1)   
conn, client_addr = server.accept()

print(f'The client at {client_addr} has connected to the server')

# listens for requests, prints any incoming messages, and sends a response
while True:
    recv_msg = conn.recv(2048)
    
    if recv_msg:
        print(f'<{client_addr}> {recv_msg}')

