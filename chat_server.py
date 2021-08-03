# Eric Chiu
# CS 372 Summer 2021
# Client-Server Chat Implementation

import socket
import sys

# establishes server on specified host and port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

addr = '127.0.0.1'
port = 5000  

print('Listening on ' + addr + ' port ' + str(port))

# create the server using the socket module
server.bind((addr, port))
server.listen(1)   
conn, client_addr = server.accept()

print(f'The client at {client_addr} has connected to the server')
conn.send(f'Welcome to the jungle, {client_addr}')

# listens for requests, prints any incoming messages, and sends a response
while True:
    recv_msg = conn.recv(2048)
    
    # receive client msg
    if recv_msg:
        print(f'{client_addr} >{recv_msg}')

        # if client sent the quit command
        if recv_msg == '/q':
            print('Thanks for stopping by! The connection is being terminated')
            conn.close()
            server.close()
            exit()

    # process and send msg from server
    send_msg = input(f'{addr} >')

    while len(send_msg) < 1 or len(send_msg) > 200:
        print('Error! Your message must be between 1 and 200 characters')
        send_msg = input(f'{addr} >')

    if send_msg == '/q':
            print('Thanks for stopping by! The connection is being terminated')
            conn.close()
            server.close()
            exit()
    else:
        print(f'{addr} >')
        conn.send(send_msg)
