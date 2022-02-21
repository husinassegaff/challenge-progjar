# Soal

Modifikasi server dan client sehingga setiap kali client mengirimkan pesan kepada server, server akan menyimpan setiap informasi koneksi dan pesan yang diterima ke dalam sebuah log file.

# Solusi

## A. Client

- Membuat template untuk menyiapkan alamat IP client, socket, dan pesan yang ingin dikiriman

  ```py
  import socket

  server_address = ('localhost', 5000)
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect(server_address)

  strsend = "Hi...."
  client_socket.send(strsend.encode())
  client_socket.close()
  ```

## B. Server

- Membuat template untuk menyiapkan alamat IP server, socket, dan penerimaan pesan dari client

  ```py
  import socket
  import sys
  import time

  server_address = ('localhost', 5000)
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind(server_address)
  server_socket.listen(5)
  ```

- Kemudian, untuk pengaturan log dapat disimpan dengan rincian,
  - alamat IP client bisa didapat dari `client_address[0]`
  - Port client bisa didapatkan dari `server_address[1]`
  - timsetamp dapat menggunakan `import time`
  - dan pesan didapatkan dari `recv` yang diterima dari client
- Lalu, disimpan dalam variabel `sum` dengan format `IP Client - Port Client - Timestamp - Message`

  ```py
      while True:
          client_socket, client_address = server_socket.accept()

          data = client_socket.recv(1024).decode()
          timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

          sum = client_address[0] + ' - ' + \
              str(server_address[1]) + ' - ' + str(timestamp) + ' - ' + str(data)

  ```

- Setelah itu, membuat file dengan format .txt untuk menyimpan log yang sudah disimpan. Metode yang digunakan adalah append
  ```py
  with open('log.txt', 'a') as f:
              f.write(sum)
              f.write('\n')
  ```
