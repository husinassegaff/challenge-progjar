# Soal

Modifikasi server dan client sehingga setiap kali client mengirimkan pesan kepada server, server akan menyimpan setiap informasi koneksi dan pesan yang diterima ke dalam sebuah log file.

# Solusi

## A. Client

- Pertama, import `socket` yang merupakan _low level networking interface_

  ```py
  import socket
  ```

- Kemudian tentukan alamat dan port dari server yang disimpan pada variabel `server_address` yang berupa tuple
  ```py
  server_address = ('localhost', 5000)
  ```
- Lalu, membuat variabel `client_socket` sebagai socket dari client. Adapun maksud dari `AF_INET` adalah socket antara dua proses yang bisa berjalan pada _host_ yang berbeda menggunakan IPv4. Dan `SOCK_STREAM` merupakan tipe socket untuk TCP. Setelah itu, dihubungkan dengan IP dan port server
  ```py
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect(server_address)
  ```
- Selanjutnya menyiapkan pesan yang ingin dikirimkan. Kemudian pesan di-encode dengan default-nya UTF-8 dan dikirim. Socket untuk client juga ditutup karena sudah tidak akan mengirimkan apa-apa lagi.
  ```py
  strsend = "Hi...."
  client_socket.send(strsend.encode())
  client_socket.close()
  ```

## B. Server

- Import socket dan beberapa modul yang diperlukan
  ```py
  import socket
  import sys
  import time
  ```
- Kemudian, sama seperti client. membuat variabel yang berperan sebagai socket server
  ```py
  server_address = ('localhost', 5000)
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  ```
- Selanjutnya, dilakukan `bind` atau pemberian alamat IP dan port ke socket. Dan juga dapat diatur antrian koneksi client yang dapat masuk menggunakan `listen`
  ```py
  server_socket.bind(server_address)
  server_socket.listen(5)
  ```
- Lalu disini server menerima pesan sekaligus alamat dari client, yang mana pesan disimpan pada variabel `client_socket` dan alamat client di `client_address`. untuk pesan harus di-decode terlebih dahulu.
  ```py
  client_socket, client_address = server_socket.accept()
  ```
- maka untuk pengaturan log dapat disimpan dengan rincian,
  - alamat IP client bisa didapat dari indeks tuple `client_address[0]`
  - Port client bisa didapatkan dari indeks tuple `server_address[1]`
  - timsetamp dapat diambil dengan menggunakan `time.strftime()`
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

- Setelah itu, membuat file dengan format .txt untuk menyimpan log yang sudah disimpan. Metode yang digunakan adalah _append_
  ```py
  with open('log.txt', 'a') as f:
              f.write(sum)
              f.write('\n')
  ```
