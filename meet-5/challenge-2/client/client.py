from ipaddress import ip_address
import os
import socket
import select
import sys
from threading import Thread

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8081
server.connect((ip_address, port))


def send_msg(sock):
    while True:
        strsend = input()
        word = "send"
        namefile = ''
        if word in strsend:
            namefile = strsend[5:len(strsend)]
            sock.send(f"{namefile}".encode())

            with open(namefile, "rb") as f:
                while True:
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        break

                    sock.sendall(bytes_read)

        # sock.send(data.encode())
            sys.stdout.write('<You> ')
            sys.stdout.write(namefile)
            sys.stdout.write(' already sent')
            sys.stdout.flush()


def recv_msg(sock):
    while True:
        # data = sock.recv(2048)
        received = sock.recv(BUFFER_SIZE).decode()
        if received:
            filepath, filename = received.split(SEPARATOR)
            filename = filepath + "received/" + filename

            with open(filename, "wb") as f:
                while True:
                    bytes_read = sock.recv(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    print("ini bytes_read")
                    f.write(bytes_read)

            sys.stdout.write("File Received: ")
            sys.stdout.write(filename)


Thread(target=send_msg, args=(server,)).start()
Thread(target=recv_msg, args=(server,)).start()


while True:
    sockets_list = [server]
    read_socket, write_socket, error_socket = select.select(
        sockets_list, [], [])
    for socks in read_socket:
        if socks == server:
            recv_msg(socks)
        else:
            send_msg(socks)


server.close()
