# Eric Chiu
# CS 372 Summer 2021
# Client-Server Chat Implementation

import socket
import sys

host = str(sys.argv[1])
port = str(sys.argv[2])

# establishes server on specified host and port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)   
print('Listening on ' + host + ' port ' + str(port))

# listens for requests, prints any incoming messages, and sends a response
while True:
    conn, addr = server.accept()
    msg = conn.recv(1024)
    print(msg)


    conn.close()    # terminates socket connection