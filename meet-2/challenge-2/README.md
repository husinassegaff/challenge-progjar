# Soal

Modifikasi server dan client dengan kriteria,

1. Client bisa menginput IP dan port server yang dituju
2. Server menyimpan log dari setiap pesan yang masuk
3. Setiap kali client mengirimkan pesan, server akan mengirimkan _acknowledgement_ kepada client berupa, timestamp, IP client, Port client, dan pesan. _acknowledgement_ akan ditampilkan pada layar client sebagai penanda bahwa pesan sudah diterima server
4. Ketika client mengirimkan `asklog`, maka server akan mengirimkan keseluruhan isi file log ke client. Dan client menampilkan ke layar

# Solusi

## No 1

- Dengan menggunakan metode `input()` yang sudah tersedia dari python. Kemudian, nanti disimpan pada variabel tuple
  ```py
  serverIP = input("Ini IP:")
  serverPort = int(input("Ini Port:"))
  server_address = (serverIP, serverPort)
  ```

## No 2

- Juga menggunakan metode `input()` dan disimpan pada variabel. Kemudian, di-encode serta dikirim ke server melalui socket
  ```py
  strsend = input("Ini Pesan:")
  client_socket.send(strsend.encode())
  ```

## No 3

- menggunakan method `recv()` dari socket dan di-decode untuk menerima pesan _acknowledgement_ dari server yang berisi log
  ```py
  textLog = client_socket.recv(1024).decode()
  print(textLog)
  ```

## No 4

- Server

  - menggunakan fungsi `open()` dengan metode `a` atau _append_ untuk membuat file atau menambah isi dari file. File diisi dengan setiap log yang dikirim dari client

  ```py
  client_socket, client_address = server_socket.accept()

  data = client_socket.recv(1024).decode()
  timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

  sum = client_address[0] + ' - ' + \
      str(server_address[1]) + ' - ' + str(timestamp) + ' - ' + str(data)

  with open('log.txt', 'a') as f:
      f.write(sum)
      f.write('\n')
  ```

- Client
  - selesai server mengirimkan _acknowledgement_ dan muncul di client, maka ada input apabila client butuh log secara keseluruhan. Disini menggunakan `if else` untuk memeriksa jika inputnya berupa string `asklog`, maka akan dikirimkan seluruh log yang telah disimpan sebelumnya. Apabila bukan, maka akan lanjut input pesan lagi untuk dikirimkan ke server.
  ```py
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
  ```
