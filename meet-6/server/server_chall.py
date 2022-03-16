import os
import socket
import select

UDP_IP = "127.0.0.1"
IN_PORT = 5000
timeout = 2
SEPARATOR = "<SEPARATOR>"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode()
    if data:
        file_name, filesize = data.split(SEPARATOR)
        # print ("File name + size:", data)

    f = open(file_name, 'wb')

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
            percentage = os.path.getsize(file_name)/int(filesize) * 100
            print(str(percentage) + '%')
        else:
            print (file_name + " Finish!")
            f.close()
            percentage_final = os.path.getsize(file_name)/int(filesize) * 100
            filesize_final = str(percentage_final)
            sock.sendto(filesize_final.encode(), addr)
            break