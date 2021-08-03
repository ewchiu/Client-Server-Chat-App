# Eric Chiu
# CS 372 Summer 2021
# Client-Server Chat Implementation
# Server side of chat
# Referenced https://www.geeksforgeeks.org/simple-chat-room-using-python/

import socket

addr = '127.0.0.1'
port = 5000 

# establishes server on specified host and port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(f'Listening on {addr} port {port}')

# create the server using the socket module
server.bind((addr, port))
server.listen(1)   

conn, client_addr = server.accept()

print(f'The client at {client_addr} has connected to the server')

server.close()

# listens for requests, prints any incoming messages, and sends a response
while True:
    recv_msg = conn.recv(2048).decode()
    
    # receive client msg
    if recv_msg:
        print(f'client: {recv_msg}')

        if '/q' in recv_msg:
            print('Client terminated connection')
            conn.close()
            server.close()
            exit()

    # process and send msg from server
    send_msg = input('server: ')

    while len(send_msg) < 1 or len(send_msg) > 200:
        print('Error! Your message must be between 1 and 200 characters')
        send_msg = input('server: ')

    conn.send(send_msg.encode())

    # check if we can quit
    if '/q' in send_msg:
            print('Thanks for stopping by! The connection is being terminated')
            conn.close()
            server.close()
            exit()
