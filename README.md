# Solusi Challenge Mata Kuliah Pemrograman Jaringan - B

- [Pertemuan 2](meet-2)

  1. [Challenge 1](meet-2/challenge-1) <br/>
     Modifikasi server dan client sehingga setiap kali client mengirimkan pesan kepada server, server akan menyimpan setiap informasi koneksi dan pesan yang diterima ke dalam sebuah log file.
  2. [Challenge 2](meet-2/challenge-2/) <br/>
     Modifikasi server dan client dengan kriteria,

     1. Client bisa menginput IP dan port server yang dituju
     2. Server menyimpan log dari setiap pesan yang masuk
     3. Setiap kali client mengirimkan pesan, server akan mengirimkan _acknowledgement_ kepada client berupa, timestamp, IP client, Port client, dan pesan. _acknowledgement_ akan ditampilkan pada layar client sebagai penanda bahwa pesan sudah diterima server
     4. Ketika client mengirimkan `asklog`, maka server akan mengirimkan keseluruhan isi file log ke client. Dan client menampilkan ke layar

  3. [Challenge 3](meet-2/challenge-3/) <br/>
     Membuat sebuah file `.txt` yang berisi string panjang. Kemudian, modifikasi server dan client sehingga seolah-seolah menjadi sepasang program pengirim-penerima file. Untuk urutannya,

     1. Client bisa menginput IP dan port server yang dituju
     2. Client bisa menginput nama file yang akan dikirimkan
     3. Server akan menerima semua kiriman data dari client dan kemudian merangkainya lagi menjadi file yang sama, baik isi maupun nama file aslinya

- [Pertemuan 3](meet-3)

  1. [Challenge 1](meet-3/challenge-1/) <br/>
     Modifikasi code "select"

     1. Client cukup mengetik nama file yang akan dikirim
     2. Client akan mengirimkan data (isi file) secara bertahap dalam bentuk perulangan
     3. Server menerima kiriman data dan menyusun ulang menjadi sebuah file, dan disimpan di local storage server

  2. [Challenge 2](meet-3/challenge-2/) <br/>
     Modifikasi code "select"

     1. Client cukup mengetik nama file yang akan dikirim. File berisi operasi matematika (1 operator, 2 operand). Pemisah tiap operasi adalah perpindahan baris
     2. Client akan mengirimkan data (isi file)
     3. Server menerima kiriman data, menghitung hasilnya, dan menyusun ulang menjadi sebuah file, dan disimpan di local storage di server

- [Pertemuan 4](meet-4)
  1.  [Challenge 1](meet-4/)
