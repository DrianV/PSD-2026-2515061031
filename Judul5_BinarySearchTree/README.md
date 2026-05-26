Tugas Akhir Percobaan 4

Judul Program : Program Antrian Pijat Panggilan

Program Berisi Tentang Algoritma Queue Terapis Pijat Panggilan

Source Code: 
<img width="1494" height="2306" alt="code" src="https://github.com/user-attachments/assets/cf335019-cf21-4aa1-8e73-e522d2edfd22" />

Line 1 : Bikin cetakan bernama Node buat jadi tempat angka.

Line 2 : Fungsi bawaan buat nyiapin tempat baru setiap kali kita masukin angka.

Line 3 : Nyiapin anak kiri root, awalnya masih kosong (None).

Line 4 : Nyiapin akan kanan root, awalnya juga masih kosong (None).

Line 5 : Nyimpen angka yang kita masukin ke dalam tempat angka itu (self.val).

Line 6 : Bikin fungsi bernama insert buat nambahin angka baru ke dalam pohon.

Line 7 : Ngecek, kalau posisi yang mau diincar ternyata masih kosong .

Line 8 : Karena kosong, langsung bikin kotak Node baru di situ dan selesai.

Line 9 : Ngecek, kalau angka baru ternyata lebih kecil dari angka di kotak sekarang.

Line 10 : Suruh fungsi insert nyari tempat kosong lagi ke arah sebelah kiri.

Line 11 : Ngecek, kalau angka baru ternyata lebih besar dari angka di kotak sekarang.

Line 12 : Suruh fungsi insert nyari tempat kosong lagi ke arah sebelah kanan.

Line 13 : Balikin struktur pohon yang posisinya udah rapi diperbarui.

Line 14 : Bikin fungsi inorder buat nampilin angka dari yang paling kecil ke terbesar.

Line 15 : Pastiin dulu kalau kotak yang lagi dilihat sekarang ada isinya, bukan kosong.

Line 16 : Suruh program jalan duluan ke cabang paling kiri buat nyari angka terkecil.

Line 17 : Cetak angka di kotak sekarang ke layar, terus kasih spasi di ujungnya biar ga dempet.

Line 18 : Baru deh jalan ke cabang sebelah kanan buat liat angka yang lebih besar.

Line 19 : Bikin fungsi main sebagai otak atau jalur utama jalannya program.

Line 20 : nampilin tulisan judul program di layar.

Line 21 : Perulangan terus-menerus sampai user masukin Root (angka pertama) dengan benar.

Line 22 : sistem keamanan (try) biar program ga langsung error kalau user salah ketik.

Line 23 : Munculin teks perintah dan ambil ketikan user buat angka pertama.

Line 24 : Ubah ketikan user jadi angka bulat, terus jadiin itu sebagai akar utama (root).

Line 25 : Stop perulangan bikin root karena angkanya udah bener dan sukses dibuat.

Line 26 : Bagian yang nangkep basah (except) kalau user malah ngetik huruf atau simbol.

Line 27 : Ngomelin user lewat layar kalau inputnya salah dan wajib angka bulat.

Line 28 : Kasih tau user kalau Root-nya udah berhasil dibuat.

Line 29 : Cetak petunjuk cara masukin angka selanjutnya atau cara kalau mau udahan.

Line 30 : Bikin perulangan lagi buat nerima angka-angka baru berikutnya.

Line 31 : Ambil ketikan user (bisa angka baru atau ketikan kata 'selesai').

Line 32 : Bersihin spasi liar dan ubah jadi huruf kecil semua buat ngecek kata 'selesai'.

Line 33 : Kalau user ngetik 'selesai', stop perulangan input angka baru.

Line 34 : Siapin sistem keamanan (try) kedua khusus buat jagain input angka baru.

Line 35 : Coba ubah ketikan user tadi menjadi angka bulat.

Line 36 : Panggil fungsi insert buat nyelipin angka baru itu ke dalam pohon.

Line 37 : Cetak info di layar kalau angkanya udah sukses masuk ke pohon.

Line 38 : Tangkap error kalau user ngetik yang aneh-aneh (bukan angka dan bukan kata selesai).

Line 39 : Kasih peringatan kalau inputnya salah ketik.

Line 40 : Bikin garis pembatas atas biar tampilan hasilnya rapi.

Line 41 : Cetak tulisan judul buat hasil akhir.

Line 42 : Manggil fungsi inorder buat nyetak semua angka dari yang terkecil sampai terbesar.

Link Video : 
Line 43 : Bikin garis pembatas penutup di bagian bawah.
Line 44 : Cetak kalimat penutup kalau programnya udah kelar semua.
Line 45 : Manggil fungsi main() di paling bawah biar semua kode di atas langsung jalan saat di-run.
