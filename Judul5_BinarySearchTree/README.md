Tugas Akhir Percobaan 5

Judul Program : Program Binary Search Tree Dasar

Program Berisi Tentang Dasar Penambahan Dan Pengurutan BST

Source Code: 
<img width="1494" height="2268" alt="code" src="https://github.com/user-attachments/assets/6d2b5ef3-d1f0-4d7b-a794-50c9c9b80799" />


Line 1 : Mendefinisikan kelas bernama Node untuk membuat struktur simpul pohon.

Line 2 : Membuat fungsi konstruktor (__init__) kelas Node yang menerima parameter key.

Line 3 : Menyiapkan variabel self.left bernilai None untuk menyimpan cabang anak sebelah kiri.

Line 4 : Menyiapkan variabel self.right bernilai None untuk menyimpan cabang anak sebelah kanan.

Line 5 : Menyimpan nilai dari parameter key ke dalam atribut objek bernama self.val.

Line 7 : Mendefinisikan fungsi insert dengan parameter root dan key untuk memasukkan data baru ke pohon.

Line 8 : Mengecek kondisi apakah posisi node pohon saat ini masih kosong (None).

Line 9 : Membuat dan mengembalikan objek Node baru jika kondisi baris 8 terpenuhi.

Line 10 : Mengecek apakah nilai key baru lebih kecil daripada nilai node saat ini (root.val).

Line 11 : Memanggil fungsi insert secara rekursif untuk menaruh data di cabang sebelah kiri (root.left).

Line 12 : Mengecek apakah nilai key baru lebih besar daripada nilai node saat ini (root.val).

Line 13 : Memanggil fungsi insert secara rekursif untuk menaruh data di cabang sebelah kanan (root.right).

Line 14 : Mengembalikan objek root pohon yang strukturnya sudah diperbarui.

Line 16 : Mendefinisikan fungsi inorder dengan parameter root untuk menelusuri pohon secara berurutan.

Line 17 : Mengecek apakah objek root saat ini ada (tidak bernilai None).

Line 18 : Memanggil fungsi inorder secara rekursif untuk memeriksa seluruh cabang bagian kiri.

Line 19 : Mencetak nilai node (root.val) secara horizontal ke samping dengan pemisah spasi (end=" ").

Line 20 : Memanggil fungsi inorder secara rekursif untuk memeriksa seluruh cabang bagian kanan.

Line 22 : Mendefinisikan fungsi utama bernama main sebagai pusat kendali jalannya program.

Line 23 : Mencetak teks judul atau header utama program ke layar terminal.

Line 24 : Memulai perulangan while tanpa henti untuk meminta input awal pembuatan akar pohon (root).

Line 25 : Membuka blok try untuk mengantisipasi error jika pengguna salah memasukkan tipe data.

Line 26 : Meminta input dari pengguna untuk nilai awal root pohon dan disimpan di variabel root_input.

Line 27 : Mengonversi input teks menjadi angka bulat (int) lalu membungkusnya menjadi objek Node utama.

Line 28 : Keluar dari perulangan while pertama menggunakan perintah break karena input root sudah sukses.

Line 29 : Menangkap kesalahan jenis data (ValueError) jika pengguna memasukkan teks non-angka pada baris 26.

Line 30 : Mencetak pesan peringatan agar pengguna hanya memasukkan angka bulat saja.

Line 32 : Mencetak notifikasi menggunakan f-string bahwa root pohon berhasil dibuat beserta nilainya.

Line 33 : Mencetak instruksi langkah selanjutnya untuk menambah angka atau mengetik 'selesai'.

Line 34 : Baris kosong untuk memberikan jarak visual pada output terminal.

Line 35 : Memulai perulangan while tanpa henti kedua khusus untuk menerima angka-angka baru berikutnya.

Line 36 : Meminta pengguna menginput angka baru atau kata kunci selesai, lalu disimpan di variabel pilihan.

Line 37 : Mengecek apakah input (setelah dihapus spasi ujungnya dan diubah ke huruf kecil) adalah kata 'selesai'.

Line 38 : Menghentikan perulangan input angka baru menggunakan break jika kondisi baris 37 benar.

Line 39 : Membuka blok try kedua untuk memvalidasi angka baru yang dimasukkan.

Line 40 : Mengonversi teks input dari variabel pilihan menjadi tipe data angka bulat (int).

Line 41 : Memanggil fungsi insert untuk memposisikan angka baru tersebut ke dalam struktur pohon.

Line 42 : Mencetak pesan sukses ke terminal bahwa angka baru berhasil ditambahkan ke pohon.

Line 43 : Menangkap kesalahan ValueError jika pengguna menginput teks acak yang bukan angka maupun kata 'selesai'.

Line 44 : Mencetak pesan peringatan bahwa input yang dimasukkan salah atau tidak valid.

Line 46 : Mencetak garis pembatas hiasan putus-putus pembuka hasil akhir.

Line 47 : Mencetak teks informasi bahwa data di bawahnya adalah hasil akhir yang berurutan.

Line 48 : Memanggil fungsi inorder(root) untuk mencetak isi pohon dari angka terkecil ke terbesar.

Line 49 : Mencetak garis pembatas hiasan putus-putus penutup hasil akhir.

Line 50 : Mencetak kalimat penutup tanda program telah selesai dijalankan seluruhnya.

Line 52 : Memanggil fungsi main() untuk memicu seluruh kode di atas agar langsung berjalan saat file dieksekusi.

Link Video : https://youtu.be/3qkEpyKemMY
