import socket

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

data, client_address = server_socket.recvfrom(1024)
data_message = data.decode()
server_socket.sendto(data_message.encode(), client_address)
print('data:' + str(data_message) + 'client address:' + str(client_address))
print('sock name' + str(server_socket.getsockname()))
