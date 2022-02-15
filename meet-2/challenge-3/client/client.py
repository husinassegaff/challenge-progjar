import socket
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time step

serverIP = input("Ini IP:")
serverPort = int(input("Ini Port:"))
server_address = (serverIP, serverPort)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)


strsend = input("Input nama file: ")
filesize = os.path.getsize(strsend)
client_socket.send(f"{strsend}{SEPARATOR}{filesize}".encode())

with open(strsend, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        client_socket.sendall(bytes_read)

client_socket.close()
