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

  1.  [Challenge 1](meet-4/) <br/>
      Modifikasi code supaya,
      1.  Client dapat mengirimkan beberapa angka ke server
      2.  Server menerima setiap angka, lalu memeriksa apakah angka tersebut bilangan prima atau bukan
      3.  Server mengirimkan jawaban **Y** apabila prima dan **N** jika bukan prima ke client

- [Pertemuan 5](meet-5)

  1.  [Challenge-1](meet-5/challenge-1/) <br/>
      Modifikasi program chat agar ketika seorang client mengirimkan sebuah teks berupa _mathematical statement_ seperti `3+5`, maka server dapat menghitung dan mengubah pesannya menjadi `3+5=8` dan diteruskan ke client
  2.  [Challenge-2](meet-5/challenge-2/) <br/>
      Modifikasi program chat dengan ketentuan,

      - Client dapat mengirimkan file ke semua client lainnya dengan sintaks `send <path file>`
      - Semua client lainnya menerima file tersebut dan disimpan di folder khusus. Di client juga akan muncul notifikasi bahwa seorang client mengirim file dan telah tersimpan
      - Nama file harus dipertahankan, tidak boleh diubah

  3.  [Challenge-3](meet-5/challenge-3/) <br/>
      Modifikasi program chat dengan ketentuan,

      - Asumsikan ketika terhubung, seorang client mempunyai ID Client (boleh diassign otomatis & client diinfokan atau input secara mandiri dari client)
      - Seorang client dapat mengirimkan pesan private ke client tertentu berdasarkan ID
      - Sintaks `private <ID tujuan> <pesan>`
