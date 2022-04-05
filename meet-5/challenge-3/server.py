from ipaddress import ip_address
import socket
from sqlite3 import connect
import threading
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = "127.0.0.1"
port = 8000
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []

def clientthread(conn, addr):
    while True:
        try:
            message = conn.recv(2048).decode()
            if message:
                if message:
                    client_port = addr[1]
                    client_id = client_port
                    # Target$Message
                    args = message.split("$")
                    target_id = args[0]
                    chat = args[1]
                    sys.stdout.write(f"Client ID {client_id} to {target_id}: {chat}")
                    sys.stdout.flush()
                    send_private(target_id, str(client_id) + ": " + chat)
            else:
                remove(conn, addr)
        except:
            continue

def send_private(target_id, message):
    for clients in list_of_clients:
        conn = clients[0]
        addr = clients[1]
        client_port = addr[1]
        if int(client_port) == int(target_id):
            try:
                conn.send(message.encode())
            except:
                conn.close()
                remove(conn, addr)

def remove(connection, addr):
    if [connection, addr] in list_of_clients:
        list_of_clients.remove([connection, addr])

while True:
    conn, addr = server.accept()
    list_of_clients.append([conn, addr])
    print(addr[0] + " connected")
    chat = "Your ID is " + str(addr[1]) + "\n"
    conn.send(chat.encode())
    threading.Thread(target=clientthread, args=(conn, addr)).start()

conn.close()