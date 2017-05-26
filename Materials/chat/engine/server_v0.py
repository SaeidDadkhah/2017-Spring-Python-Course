import socket

server_port = 31066
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print('Chat server started on port {}.'.format(server_port))

client_socket, address = server_socket.accept()
while True:
    received = client_socket.recv(1024)
    print(received)
    send = input('Send message: ')
    client_socket.send(send.encode('ascii'))

