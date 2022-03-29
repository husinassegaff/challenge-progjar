import socket
import select
import sys
from threading import Thread
import time
import shutil
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8000
server.connect((ip_address, port))

file_recv_state = 0
file_session = None
file_name = ""
id = "client2"
SEPARATOR = "<SEPARATOR>"


def send_msg(sock):
    while True:
        data = sys.stdin.readline()
        if(data.__contains__("SEND")):
            file_name = data[5:].rstrip("\n")
            sock.send(file_name.encode())
            time.sleep(2)
            f = open(file_name, "r")
            file_data = f.read()
            f.close()
            sys.stdout.write('<' + file_name + '>' 'Already Sent')
            sys.stdout.flush()
            sock.send(file_data.encode())
        elif(data.__contains__("LIST")):
            flag = '3'
            sock.send(flag.encode())
        elif(data.__contains__("DOWNZIP")):
            flag = '4'
            sock.send(flag.encode())
        elif(data.__contains__("LOG")):
            flag = '6'
            sock.send(flag.encode())
        else:
            data = f"5{data}{SEPARATOR}{id}"
            sock.send(data.encode())
            sys.stdout.flush()


def recv_msg(sock):
    while True:
        data = sock.recv(2048).decode().rstrip("\n")
        data = str(data)
        global file_recv_state
        global file_session
        global file_name
        if data == '3':
            path = "C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/shared"
            os.listdir(path)
            sys.stdout.write('<Server> List Directory: ')
            for file in os.listdir(path):
                i = 1
                sys.stdout.write(str(i) + '. ' + file)
                i += 1
                sys.stdout.flush()

        elif data == '4':
            dir_name = "C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/shared"
            shutil.make_archive('shared', 'zip', dir_name)

            file_name = "shared.zip"

            folder_shared = os.path.join(
                r'C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/', file_name)
            folder_src = os.path.join(
                r'C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/client2/', file_name)
            shutil.move(folder_src, folder_shared)

            sys.stdout.write('<Server> Download Zip: ' + file_name)
            sys.stdout.flush()

        elif data.__contains__('5'):
            msg, addr = data.split(SEPARATOR)
            sys.stdout.write('<' + addr + '> ' + msg[1:])
            sys.stdout.flush()

        elif data.__contains__('6'):
            sys.stdout.write(
                '<Server> ' + "log.txt Downloaded in folder Shared")
            sys.stdout.flush()

        elif file_recv_state == 0:
            file_name = data
            sys.stdout.write('<' + data + '> received')
            sys.stdout.flush()
            file_session = open(data, "w")
            file_recv_state = 1

        elif file_recv_state == 1:
            if data:
                file_session.write(data)
                file_recv_state = 0
                file_session.close()

                folder_shared = os.path.join(
                    r'C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/shared/', file_name)
                folder_src = os.path.join(
                    r'C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/client2/', file_name)
                shutil.move(folder_src, folder_shared)


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
