import os
import socket
import time

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024

strsend = input("Input nama file: ")
filesize = os.path.getsize(strsend)
client_socket.sendto(f"{strsend}{SEPARATOR}{filesize}".encode(), server_address)
delay = 1

f = open(strsend, "r")
data = f.read(BUFFER_SIZE)
while(data):
    if(client_socket.sendto(data.encode(), server_address)):
        data = f.read(BUFFER_SIZE)
        time.sleep(0.02) # Give receiver a bit time to save

recv_message, server_address = client_socket.recvfrom(1024)
print(str(recv_message.decode()) + "%")
