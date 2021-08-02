# Eric Chiu
# CS 372 Summer 2021
# Client-Server Chat Implementation

import socket
import sys

host = str(sys.argv[1])
port = str(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(host, port)

while True:
    sock = [sys.stdin, client]

