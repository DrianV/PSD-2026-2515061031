Tugas Akhir Percobaan 5 

Judul Program : Program Kelola Database Mahasiswa

Program berisi tentang penambahan , pengurangan data dalam database mahasiswa

Source Code:
<img width="1850" height="3218" alt="SOAL TA 6 PSD" src="https://github.com/user-attachments/assets/2f56cc5b-2dc9-4875-bd1f-4bccfb5df695" />

Line 1 : Mendefinisikan fungsi tampilkan_semua_data dengan parameter database_mahasiswa.

Line 2 : Mencetak header teks untuk daftar mahasiswa ke layar.

Line 3 : Memeriksa apakah database_mahasiswa kosong (tidak memiliki data).

Line 4 : Mencetak teks "(Database kosong)" jika kondisi pada Line 3 terpenuhi.

Line 5 : Blok alternatif (else) jika dictionary ternyata berisi data.

Line 6 : Melakukan perulangan untuk mengambil pasangan key (npm) dan value (nama) dari data mahasiswa.

Line 7 : Mencetak data NPM dan Nama mahasiswa hasil perulangan ke layar.

Line 8 : Mencetak garis pembatas sebagai penutup menu daftar mahasiswa.

Line 10 : Mendefinisikan fungsi cari_mahasiswa dengan parameter database_mahasiswa.

Line 11 : Mencetak header teks untuk menu pencarian data mahasiswa.

Line 12 : Mengambil input NPM yang ingin dicari dari user dan menghapus spasi di awal/akhir input.

Line 14 : Memeriksa apakah NPM yang dicari ada di dalam dictionary database_mahasiswa.

Line 15 : Mencetak nama mahasiswa jika NPM tersebut ditemukan di dalam database.

Line 16 : Blok alternatif (else) jika NPM tidak ditemukan.

Line 17 : Mencetak pesan peringatan bahwa data mahasiswa tidak ditemukan.

Line 19 : Mendefinisikan fungsi tambah_mahasiswa dengan parameter database_mahasiswa.

Line 20 : Mencetak header teks untuk menu tambah data mahasiswa baru.

Line 21 : Mengambil input NPM baru dari user dan membersihkan spasi di awal/akhir teks.

Line 23 : Memeriksa apakah user mengosongkan input NPM baru.

Line 24 : Mencetak pesan kesalahan bahwa NPM tidak boleh kosong.

Line 25 : Menghentikan fungsi lebih awal (return) agar proses input dibatalkan.

Line 26 : Memeriksa apakah NPM baru yang dimasukkan sudah digunakan oleh mahasiswa lain.

Line 27 : Mencetak pesan kesalahan bahwa NPM sudah terdaftar beserta nama pemiliknya.

Line 28 : Blok alternatif (else) jika NPM baru valid dan belum pernah digunakan.

Line 29 : Mengambil input Nama Mahasiswa baru dari user dan membersihkan spasi di awal/akhir teks.

Line 30 : Memeriksa apakah user mengosongkan input nama mahasiswa baru.

Line 31 : Mencetak pesan kesalahan bahwa nama tidak boleh kosong.

Line 32 : Menghentikan fungsi lebih awal (return) agar proses input dibatalkan.

Line 33 : Menyimpan data baru ke dalam dictionary dengan npm_baru sebagai key dan nama_baru sebagai value.

Line 34 : Mencetak pesan sukses bahwa data mahasiswa baru berhasil ditambahkan.

Line 36 : Mendefinisikan fungsi hapus_mahasiswa dengan parameter database_mahasiswa.
Line 37 : Mencetak header teks untuk menu hapus data mahasiswa.

Line 38 : Mengambil input NPM yang ingin dihapus dari user dan membersihkan spasi di awal/akhir teks.

Line 40 : Memeriksa apakah NPM yang ingin dihapus tersedia di dalam database.

Line 41 : Menghapus data menggunakan .pop(npm_hapus) dan menyimpan nama yang dihapus ke variabel nama_terhapus.

Line 42 : Mencetak pesan sukses bahwa data mahasiswa dengan NPM tersebut telah dihapus.

Line 43 : Blok alternatif (else) jika NPM yang akan dihapus tidak ditemukan.

Line 44 : Mencetak pesan kesalahan bahwa proses hapus gagal karena data tidak ditemukan.

Line 46 : Membuat variabel global db_kampus berupa dictionary (Hash Map) untuk menyimpan data mahasiswa.

Line 47 : Mengisi data mahasiswa pertama dengan key "001" dan value "Wira".

Line 48 : Mengisi data mahasiswa kedua dengan key "002" dan value "Aldi".

Line 49 : Mengisi data mahasiswa ketiga dengan key "003" dan value "Andra".

Line 52 : Memulai perulangan terus-menerus (while True) untuk menampilkan menu utama secara berulang.

Line 53 : Mencetak garis pembatas atas untuk tampilan menu.

Line 54 : Mencetak judul menu "SISTEM AKADEMIK KAMPUS (HASH)".
Line 55 : Mencetak garis pembatas tengah menu.

Line 56 : Mencetak pilihan menu 1: Cari Mahasiswa.

Line 57 : Mencetak pilihan menu 2: Tambah Mahasiswa Baru.

Line 58 : Mencetak pilihan menu 3: Hapus Data Mahasiswa.

Line 59 : Mencetak pilihan menu 4: Lihat Semua Data.

Line 60 : Mencetak pilihan menu 5: Keluar.

Line 61 : Mencetak garis pembatas bawah untuk tampilan menu.

Line 63 : Mengambil input pilihan menu angka (1-5) dari user dan membersihkan spasi di awal/akhir teks.

Line 65 : Memeriksa apakah user memilih menu "1".

Line 66 : Memanggil fungsi cari_mahasiswa dengan mengirimkan data db_kampus.

Line 67 : Memeriksa apakah user memilih menu "2".

Line 68 : Memanggil fungsi tambah_mahasiswa dengan mengirimkan data db_kampus.

Line 69 : Memeriksa apakah user memilih menu "3".

Line 70 : Memanggil fungsi hapus_mahasiswa dengan mengirimkan data db_kampus.

Line 71 : Memeriksa apakah user memilih menu "4".

Line 72 : Memanggil fungsi tampilkan_semua_data dengan mengirimkan data db_kampus.

Line 73 : Memeriksa apakah user memilih menu "5".

Line 74 : Mencetak kalimat penutup program sebagai tanda terima kasih.

Line 75 : Menghentikan perulangan while menggunakan perintah break untuk keluar dari program.

Line 76 : Blok alternatif (else) jika user memasukkan input di luar angka 1 sampai 5.

Line 77 : Mencetak pesan kesalahan bahwa pilihan menu yang dimasukkan tidak valid.

Link Video : https://youtu.be/QRKsORNVJ7Y
