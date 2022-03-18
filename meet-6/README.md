# Soal

Buatlah simulasi pengiriman file dengan menggunakan UDP (tanpa connect, menggunakan send-to dan recv-from) yang filenya dipecah menggunakan blok pengiriman per 1 kb (1024).

Client dapat memilih file yang akan dikirim dengan ukuran file minimal 10MB. Kemudian, syarat lainnya,

1. Proses pengiriman diawali dengan mengirimkan nama file dan ukuran asli file
2. Kemudian, client mengirimkan isi file secara bertahap dengan blok per 1 kb, dan server menggabungkannya manual secara bertahap menjadi sebuah file
3. Di akhir pengiriman (server setelah menerima akhir file) akan menampilkan berapa % data yang berhasil dikirimkan dari file tersebut

# Solusi
