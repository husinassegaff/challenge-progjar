import socket
import sys
import time

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

try:
    while True:
        client_socket, client_address = server_socket.accept()

        data = client_socket.recv(1024).decode()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        sum = client_address[0] + ' - ' + \
            str(server_address[1]) + ' - ' + str(timestamp) + ' - ' + str(data)

        with open('log.txt', 'a') as f:
            f.write(sum)
            f.write('\n')

        client_socket.close()


except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)
