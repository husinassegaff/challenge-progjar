import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target_name = 'www.google.com'
server_address = (target_name, 80)
client_socket.connect(server_address)

request_header = 'GET / HTTP/1.0\r\nHost: ' + target_name + '\r\n\r\n'
client_socket.sendall(request_header.encode())

response = ''

while True:
    recv = client_socket.recv(1024).decode()

    if not recv:
        break
    response += recv

print(response)
client_socket.close()
