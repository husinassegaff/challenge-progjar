# Soal

Modifikasi server dan client dengan kriteria,

1. Client bisa menginput IP dan port server yang dituju
2. Server menyimpan log dari setiap pesan yang masuk
3. Setiap kali client mengirimkan pesan, server akan mengirimkan _acknowledgement_ kepada client berupa, timestamp, IP client, Port client, dan pesan. _acknowledgement_ akan ditampilkan pada layar client sebagai penanda bahwa pesan sudah diterima server
4. Ketika client mengirimkan `asklog`, maka server akan mengirimkan keseluruhan isi file log ke client. Dan client menampilkan ke layar

# Solusi
