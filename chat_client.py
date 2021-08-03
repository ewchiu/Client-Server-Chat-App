# Eric Chiu
# CS 372 Summer 2021
# Client-Server Chat Implementation
# Client side of chat
# Referenced https://www.geeksforgeeks.org/simple-chat-room-using-python/

import socket

addr = '127.0.0.1'
port = 5000   

# establishes server on specified host and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((addr, port))  
print(f'You are connecting to {addr} port {port}, kick it off by sending a message!')

while True:
    # send a message to the server
    msg = input('client: ')

    client.send(msg.encode())

    if '/q' in msg:
        print('Terminating connection')
        client.close()
        exit()
    else:
        # receive and print message from the server
        recv_msg = client.recv(2048).decode()
        print(f'server: {recv_msg}')

        if '/q' in recv_msg:
            print('Server terminated connection')
            client.close()
            exit()
