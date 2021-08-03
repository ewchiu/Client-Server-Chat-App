# Eric Chiu
# CS 372 Summer 2021
# Client-Server Chat Implementation

import socket
import sys

# establishes server on specified host and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = '127.0.0.1'
port = 5000   

client.connect((addr, port))  
print('Listening on ' + addr + ' port ' + str(port))

