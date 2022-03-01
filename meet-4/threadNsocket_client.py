import pickle
import socket
import sys

server_address = ('localhost', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

try:
    while True:
        array = []
        n = int(input("Masukkan jumlah elemen:"))
        for i in range(n):
            array.append(str(input()))

        for i in range(n):
            client_socket.send(array[i].encode())
            sys.stdout.write(client_socket.recv(1024).decode())
        print('\n')


except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)




