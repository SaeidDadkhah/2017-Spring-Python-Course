import socket


class ChatClient:
    def __init__(self, server_name, server_port):
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client_socket.connect((server_name, server_port))

    def get_name(self):
        return self.__client_socket.getsockname()

    def send_message(self, message):
        self.__client_socket.send(message)

    def receive_message(self):
        try:
            return self.__client_socket.recv(1024)
        except (ConnectionAbortedError, OSError):
            return None

    def close(self):
        self.__client_socket.close()


if __name__ == "__main__":
    import time
    from threading import Thread

    def send_messages(client: ChatClient):
        i = 0
        while True:
            time.sleep(2)
            client.send_message('{}'.format(i).encode('ascii'))
            print(i)
            i += 1

    sn = 'localhost'
    sp = 31066
    c = ChatClient(sn, sp)
    t1 = Thread(target=lambda: send_messages(c))
    t1.start()
    while True:
        print(c.receive_message())
