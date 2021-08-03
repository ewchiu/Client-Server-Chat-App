# Eric Chiu
# CS 372 Summer 2021
# Client-Server Chat Implementation

import socket
import sys

addr = '127.0.0.1'
port = 5000   

# establishes server on specified host and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((addr, port))  

while True:
    msg = input('client: ')

    client.send(msg.encode())

    if '/q' in msg:
        print('Terminating connection')
        client.close()
        exit()
    else:
        recv_msg = client.recv(2048).decode()
        print(f'server: {recv_msg}')

        if '/q' in recv_msg:
            print('Terminating connection')
            client.close()
            exit()
