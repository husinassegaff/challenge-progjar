# Soal

Modifikasi code "select"

1. Client cukup mengetik nama file yang akan dikirim
2. Client akan mengirimkan data (isi file) secara bertahap dalam bentuk perulangan
3. Server menerima kiriman data dan menyusun ulang menjadi sebuah file, dan disimpan di local storage server

# Solusi

## No 1 & 2

- Membuat variabel untuk menyimpan nama file yang diinput client, lalu file tersebut dibuka dan dikirim ke server baris per baris dengan menggunakan looping

  ```py
  namefile = str(input())

  f = open(namefile, 'r')
  lines = f.readlines()

  for line in lines:
    client_socket.send(line.encode())
    sys.stdout.write(client_socket.recv(1024).decode())
    sys.stdout.write('>> ')
  ```

## No 3

- Untuk sisi server saat menerima data akan melakukan `append` pada file yang telah disiapkan dan melakukan _write_ per baris menggunakan fungsi `writelines()`

  ```py
  data = sock.recv(1024).decode()

  file1 = open('myfile.txt', 'a')
  file1.writelines(data)
  file1.close()

  ```
