# Soal

Modifikasi code "select"

1. Client cukup mengetik nama file yang akan dikirim. File berisi operasi matematika (1 operator, 2 operand). Pemisah tiap operasi adalah perpindahan baris
2. Client akan mengirimkan data (isi file)
3. Server menerima kiriman data, menghitung hasilnya, dan menyusun ulang menjadi sebuah file, dan disimpan di local storage di server

# Solusi

## No 1 & 2

- Membuat variabel untuk menyimpan nama file yang diinput client, lalu file tersebut dibuka dan dikirim ke server baris per baris dengan menggunakan looping. Disini juga ketika setiap baris akan dikirim, dihapus karakter di akhir string yang berupa `\n` agar saat di server hanya karakter angka dan operator.
  ```py
  filename = str(input())
          with open(filename) as f:
              lines = [line.rstrip('\n') for line in f]
              print(lines)
              for number in lines:
                  client_socket.send(number.encode())
                  sys.stdout.write(client_socket.recv(1024).decode())
  ```

## No 3

- Pada sisi server, ketika menerima data per baris dari client, maka akan dilakukan operasi matematika menggunakan fungsi `eval()` yang sudah tersedia di python. Kemudian, disimpan dalam file
  ```py
  data = sock.recv(1024).decode()
  print(str(sock.getpeername()), str(data))
  with open('result.txt', 'a') as the_file:
    the_file.write(str(data) + "=" + str(eval(data)) + "\n")
  ```
