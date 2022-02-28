# Soal

Membuat sebuah file `.txt` yang berisi string panjang. Kemudian, modifikasi server dan client sehingga seolah-seolah menjadi sepasang program pengirim-penerima file. Untuk urutannya,

1. Client bisa menginput IP dan port server yang dituju
2. Client bisa menginput nama file yang akan dikirimkan
3. Server akan menerima semua kiriman data dari client dan kemudian merangkainya lagi menjadi file yang sama, baik isi maupun nama file aslinya

# Solusi

## No 1

- Sama seperti [challenge-2](../challenge-2/) dengan menggunakan metode `input()`
  ```py
  serverIP = input("Ini IP:")
  serverPort = int(input("Ini Port:"))
  server_address = (serverIP, serverPort)
  ```

## No 2

- Dibuat variabel baru untuk menyimpan input nama file dari client
  ```py
  strsend = input("Input nama file: ")
  ```
- Kemudian, menggunakan modul `os` untuk mendapatkan size dari file yang akan dikirimkan. Dan kemudian menggunakan variabel `client_socket` yang sudah diinisiasi sebagai socket dari client untuk mengirimkan file tersebut
  ```py
  SEPARATOR = "<SEPARATOR>"
  filesize = os.path.getsize(strsend)
  client_socket.send(f"{strsend}{SEPARATOR}{filesize}".encode())
  ```
- Diatur sekali pengiriman sebanyak 4096 bytes saat proses pengiriman dengan perulangan while

  ```py
  BUFFER_SIZE = 4096  # send 4096 bytes each time step

  with open(strsend, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        client_socket.sendall(bytes_read)
  ```

### No 3

- pada server menerima setiap pengiriman isi file dari client dengan maksimal byte 4096. Kemudian, ditulis ulang menggunakan metode `wb` atau membuka file dalama binary format dan akan ditulis.

  ```py
  while True:
    client_socket, client_address = server_socket.accept()

    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            # write to the file the bytes we just received
            f.write(bytes_read)

    client_socket.close()
  ```
