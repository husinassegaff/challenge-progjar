import socket
import sys

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

sys.stdout.write('>> ')

try:
    while True:
        filename = str(input())
        with open(filename) as f:
            lines = [line.rstrip('\n') for line in f]
            print(lines)
            for number in lines:
                client_socket.send(number.encode())
                sys.stdout.write(client_socket.recv(1024).decode())


except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)
