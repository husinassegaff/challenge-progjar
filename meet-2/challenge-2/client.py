import socket

serverIP = input("Ini IP:")
serverPort = int(input("Ini Port:"))
server_address = (serverIP, serverPort)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    strsend = input("Ini Pesan:")
    client_socket.send(strsend.encode())

    textLog = client_socket.recv(1024).decode()
    print(textLog)

    ask_log = str(input())
    if(ask_log == "asklog"):
        a_file = open("log.txt")
        lines = a_file.readlines()
        for line in lines:
            print(line)
        a_file.close()
        break
    else:
        continue
client_socket.close()
