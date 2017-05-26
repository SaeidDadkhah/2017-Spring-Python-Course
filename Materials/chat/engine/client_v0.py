import socket

server_name = 'localhost'
server_port = 31066
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_name, server_port))
while True:
    send = input('Send message: ')
    client_socket.send(send.encode('ascii'))
    received = client_socket.recv(1024)
    print('Received message: %s' % received)
