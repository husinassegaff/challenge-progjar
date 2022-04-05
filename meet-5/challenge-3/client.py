import socket
import select
import sys
from threading import Thread

client_id = None

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8000
server.connect((ip_address, port))

def send_msg(sock):
    while True:
        global client_id
        command = sys.stdin.readline()
        args = command.split(" ")
        if args[0] == "private":
            # args[1] : Tujuan
            # args[2] : Message
            temp = args[1] + "$" + args[2]
            sock.send(temp.encode())
                
def recv_msg(sock):
    while True:
        data = sock.recv(2048)
        sys.stdout.write(data.decode())
        sys.stdout.flush()

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

