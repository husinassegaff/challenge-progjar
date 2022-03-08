import os
import socket
import select
import sys
import threading

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = '127.0.0.1'
port = 8081
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []


def clientthread(conn, addr):
    while True:
        try:
            received = conn.recv(BUFFER_SIZE).decode()
            if received:
                filename = received
                filename = os.path.basename(filename)

                # with open(filename, "wb") as f:
                #     while True:
                #         # read 1024 bytes from the socket (receive)
                #         bytes_read = conn.recv(BUFFER_SIZE)
                #         if not bytes_read:
                #             print("Salah disini")
                #             break
                #         # write to the file the bytes we just received
                #         print("ini bytes_read :")
                #         f.write(bytes_read)

                print('<' + addr[0] + '> ' + "sent file :" + filename)
                broadcast(filename, conn)
            else:
                remove(conn)

        except:
            continue


def broadcast(filename, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                filepath = "C:/Users/husin/Documents/Coding/Kuliah/Sem6/Progjar/challenge-progjar/meet-5/challenge-2/client/"
                filename_send = filepath + filename
                clients.send(f"{filepath}{SEPARATOR}{filename}".encode())

                with open(filename_send, "rb") as f:
                    while True:
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            print("break")
                            # file transmitting is done
                            break
                        print("ada text disini")
                        clients.sendall(bytes_read)

            except:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + ' connected')
    threading.Thread(target=clientthread, args=(conn, addr)).start()
