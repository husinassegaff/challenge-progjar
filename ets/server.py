from ipaddress import ip_address
import socket
from sqlite3 import connect
import threading
import select
import sys
import os
import shutil

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = "127.0.0.1"
port = 8000
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []

history_chat = []

SEPARATOR = "<SEPARATOR>"


def clientthread(conn, addr):
    while True:
        try:
            message = conn.recv(2048).decode()
            if message:

                # Response Server untuk perintah  LIST
                if message == '3':
                    path = "C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/shared"
                    os.listdir(path)
                    sys.stdout.write('<Server> List Directory: ')
                    for file in os.listdir(path):
                        i = 1
                        sys.stdout.write(str(i) + '. ' + file)
                        i += 1
                        sys.stdout.flush()
                    broadcast(message + "\n", conn)

                # Response Server untuk perintah  DOWNZIP
                elif message == '4':
                    print("<Server> Download zip")
                    dir_name = "C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/shared"
                    shutil.make_archive('shared', 'zip', dir_name)
                    broadcast(message + "\n", conn)

                # Response Server untuk perintah  chat biasa
                elif (message.__contains__('5')):
                    message, address = message.split(SEPARATOR)
                    history_chat.append('<' + address + '>' + message[1:])
                    print('<' + address + '> ' + message[1:])
                    message = f"{message}{SEPARATOR}{address}"
                    broadcast(message + "\n", conn)

                # Response Server untuk perintah  LOG
                elif message == '6':
                    print("<Server> Create Log")
                    for i in history_chat:
                        f = open("log.txt", "a")
                        f.write(i)
                        f.close()

                    file_name = "log.txt"

                    folder_shared = os.path.join(
                        r'C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/shared/', file_name)
                    folder_src = os.path.join(
                        r'C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/ets/', file_name)
                    shutil.move(folder_src, folder_shared)

                    broadcast(message + "\n", conn)

                # Response Server untuk perintah  SEND
                elif message:
                    print("<" + addr[0] + ">" + message)

                    # message_to_send = "<" + addr[0] + ">" + message
                    broadcast(message + "\n", conn)
            else:
                remove(conn)
        except:
            continue


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + " connected")
    threading.Thread(target=clientthread, args=(conn, addr)).start()

conn.close()
