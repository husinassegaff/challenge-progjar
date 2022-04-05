import socket
import select
import sys
from threading import Thread
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8000
server.connect((ip_address, port))

file_recv_state = 0
file_session = None

def send_msg(sock):
    while True:
        data = sys.stdin.readline()
        if(data.__contains__("send")):
            file_name = data[5:].rstrip("\n")
            sock.send(file_name.encode())
            time.sleep(2)
            f = open(file_name, "r")
            file_data = f.read()
            f.close()
            sock.send(file_data.encode())
            sys.stdout.write( '<' + file_name + '>' 'Already Sent')
            #sys.stdout.write(data)
            sys.stdout.flush()
        else:
            # sock.send(data.encode())
            sys.stdout.write('<You> Invalid command')
            sys.stdout.write(data)
            sys.stdout.flush()

def recv_msg(sock):
    while True:
        data = sock.recv(2048).decode().rstrip("\n")
        global file_recv_state
        global file_session
        if file_recv_state == 0:
            sys.stdout.write('<' + data + '> received')
            sys.stdout.flush()
            file_session = open(data, "w")
            file_recv_state = 1
        else:
            if data:
                file_session.write(data)
                file_recv_state = 0
                file_session.close()

Thread(target=send_msg, args=(server,)).start()
Thread(target=recv_msg, args=(server,)).start()


while True:
    sockets_list = [server]
    read_socket, write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_socket:
        if socks == server:
            recv_msg(socks)
        else:
            send_msg(socks)

server.close()

