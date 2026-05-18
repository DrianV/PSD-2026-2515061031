Tugas Akhir Percobaan 4
Judul Program : Program Antrian Pijat Panggilan
Program Berisi Tentang Algoritma Queue Terapis Pijat Panggilan
Source code : 
<img width="1956" height="2154" alt="code" src="https://github.com/user-attachments/assets/f14e8d23-734b-4011-94c0-fd377ad9e3c5" />
Line 1: Mendefinisikan fungsi utama program bernama main.
Line 2: Membuat list kosong bernama antrian_pijat yang akan berfungsi sebagai wadah antrian (struktur data Queue).
Line 3: Menentukan variabel konstanta untuk membatasi jumlah maksimal pelanggan yang boleh mengantri dalam satu waktu.
Line 5: Memulai perulangan tak terbatas agar menu program terus muncul sampai pengguna memilih untuk keluar.
Line 6: Menghitung sisa slot yang tersedia dengan cara mengurangi batas maksimal dengan jumlah elemen yang ada di dalam list saat ini.
Line 7 - 11 : Menampilkan judul program, informasi sisa kuota, dan daftar menu (1-4) ke layar pengguna.
Line 13: Mengambil input dari pengguna untuk menentukan menu mana yang akan dijalankan.
Line 15: Mengecek apakah pengguna memilih menu nomor 1 (Booking Antrian).
Line 16: Memeriksa apakah jumlah pelanggan di list sudah mencapai atau melebihi batas maksimal (5 orang).
Line 17: Menampilkan pesan penolakan jika antrian sudah penuh.
Line 18: Blok yang dijalankan jika kuota antrian masih tersedia.
Line 19: Meminta input nama pelanggan baru.
Line 20: Memastikan input nama tidak hanya berisi spasi kosong (validasi input).
Line 21: Menambahkan nama pelanggan ke urutan paling belakang dalam list (konsep Enqueue).
Line 22: Memberikan konfirmasi bahwa pelanggan berhasil terdaftar beserta nomor urutnya.
Line 23 - 24: Menampilkan pesan peringatan jika pengguna tidak mengisi nama.
Line 26: Mengecek apakah pengguna memilih menu nomor 2 (Layani Pelanggan).
Line 27: Memeriksa apakah list antrian dalam keadaan kosong.
Line 28: Memberikan informasi jika tidak ada orang yang bisa dilayani.
Line 29: Blok yang dijalankan jika ada setidaknya satu pelanggan di dalam antrian.
Line 30: Menghapus dan mengambil elemen pertama (paling depan) dari list. Ini adalah prinsip FIFO (First In First Out).
Line 31: Menampilkan informasi bahwa pelanggan tersebut sedang dalam proses pelayanan.
Line 33: Mengecek apakah pengguna memilih menu nomor 3 (Lihat Daftar Antrian).
Line 34: Memeriksa apakah antrian kosong sebelum mencoba menampilkannya.
Line 35: Pesan jika daftar antrian tidak berisi siapapun.
Line 36: Blok yang dijalankan jika ada data di dalam list.
Line 37: Mencetak judul daftar antrian.
Line 38: Melakukan perulangan pada list antrian; enumerate digunakan untuk mendapatkan nomor urut yang dimulai dari angka 1.
Line 39: Mencetak nama setiap pelanggan beserta nomor antriannya.
Line 41: Mengecek apakah pengguna memilih menu nomor 4 (Keluar).
Line 42: Menampilkan pesan penutup program.
Line 43: Menghentikan paksa perulangan while True untuk keluar dari program.
Line 44: else: Blok yang menangani input selain angka 1, 2, 3, atau 4.
Line 45: Pesan peringatan jika input menu salah.
Line 47 - 48: Memastikan fungsi main() dijalankan saat file skrip ini dieksekusi secara langsung.

Link Video : https://youtu.be/DJx3YkwVSvE?si=0ERTEtd3wRDziAPy
