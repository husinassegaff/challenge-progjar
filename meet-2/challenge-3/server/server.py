import socket
import sys
import os
import time

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

try:
    while True:
        client_socket, client_address = server_socket.accept()

        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)

        with open(filename, "wb") as f:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                # write to the file the bytes we just received
                f.write(bytes_read)

        client_socket.close()


except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)
