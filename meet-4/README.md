# Soal

Modifikasi code supaya,

1. Client dapat mengirimkan beberapa angka ke server
2. Server menerima setiap angka, lalu memeriksa apakah angka tersebut bilangan prima atau bukan
3. Server mengirimkan jawaban **Y** apabila prima dan **N** jika bukan prima ke client

# Solusi

## No 1

- Membuat variabel array untuk menyimpan kumpulan angka yang akan dikirim ke server, kemudian input banyaknya angka yang ingin dikirimkan ke server. Lalu, input angka sesuai jumlah yang telah diinputkan sebelumnya.
  ```py
  array = []
  n = int(input("Masukkan jumlah elemen:"))
  for i in range(n):
    array.append(str(input()))
  ```
- Setelah itu, dilakukan looping juga untuk mengirimkan setiap angka ke server. Looping tersebut juga menerima hasil pengecekan bilangan prima dari server
  ```py
  for i in range(n):
    client_socket.send(array[i].encode())
    sys.stdout.write(client_socket.recv(1024).decode())
  ```

## No 2 dan 3

- Saat server menerima angka dari client, maka dimasukkan ke dalam fungsi `PrimeChecker()` untuk mengecek apakah angka yang dikirimkan merupakan bilangan prima atau bukan

  ```py
  def run(self):
    running = 1
    while running:
        data = self.client.recv(self.size)
        if data:
            Hasil = PrimeChecker(int(data))
            self.client.send(Hasil.encode())
        else:
            self.client.close()
            running = 0

  def PrimeChecker(a):
    # Checking that given number is more than 1
    if a > 1:
        # Iterating over the given number with for loop
        for j in range(2, int(a/2) + 1):
            # If the given number is divisible or not
            if (a % j) == 0:
                return('T')
                break
        # Else it is a prime number
        else:
            return('Y')
    # If the given number is 1
    else:
        return('T')
  ```
