import socket
import random

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)

while True:
    data, client_address = server_socket.recvfrom(1024)
    data_msg = data.decode()

    if random.randint(0, 1):
        server_socket.sendto(data_msg.encode(), client_address)
        print('data:' + str(data_msg) + 'client address:' + str(client_address))
        print('sock name' + str(server_socket.getsockname()))

    else:
        print('Server is down')
