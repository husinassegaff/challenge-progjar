import socket
from pprint import pprint

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "HI..."
client_socket.sendto(message.encode(), server_address)

recv_message, server_address = client_socket.recvfrom(1024)
print(str(recv_message.decode()) + str(server_address))
