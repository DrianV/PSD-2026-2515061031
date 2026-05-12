Tugas Akhir Percobaan 3

Judul Program : Program Pencari Nilai dan Pemiliknya

Program berisi tentang algoritma Sequential Searching untuk mencari banyaknya nilai dan siapa saja pemiliknya 

Source  Code:
<img width="1726" height="1622" alt="code" src="https://github.com/user-attachments/assets/34b76260-1818-44d7-ba72-61147daa05ae" />

1. Mendefinisikan fungsi sequential_search dengan parameter input: list nama, list nilai, jumlah elemen (n), dan nilai yang dicari (target).
2. Inisialisasi tiga variabel: i sebagai penunjuk indeks (mulai dari 0), counter untuk menghitung jumlah kecocokan, dan pemilik sebagai list kosong untuk menyimpan nama-nama yang nilainya cocok.
3. Perulangan while yang akan berjalan terus selama indeks i masih di dalam jangkauan jumlah data (n).
4. Kondisi pengecekan: Apakah elemen pada list_nilai di posisi ke-i sama dengan target
5. Jika cocok (True), tambahkan angka 1 ke variabel counter
6. Jika cocok (True), masukkan nama dari list_nama pada posisi yang sama (i) ke dalam list pemilik.
7. Menaikkan nilai i (increment) agar perulangan pindah ke elemen berikutnya
8. Setelah semua data dicek, fungsi mengembalikan (return) hasil berupa angka total kecocokan dan list nama-nama pemiliknya.
9. 
10. Mendefinisikan fungsi main sebagai titik awal eksekusi program.
11. Membuat dua list kosong (nama_mhs dan nilai_mhs) untuk menampung data yang akan diinput pengguna.
12. 
13. coba menjalankan kode
14. Meminta user memasukkan jumlah mahasiswa dan mengubahnya menjadi tipe data int
15. 
16. Memulai perulangan for sebanyak jumlah mahasiswa yang sudah ditentukan.
17. Meminta input nama mahasiswa. Format {i+1} digunakan agar tampilan di layar mulai dari angka 1 (bukan 0).
18. Meminta input nilai mahasiswa dan mengubahnya menjadi float

19-20. Menambahkan (push) data nama dan nilai yang baru saja diinput ke dalam list masing-masing.

22. Meminta user memasukkan nilai yang ingin dicari frekuensi kemunculannya.
 
24. Memanggil fungsi sequential_search. Hasil kembaliannya langsung dipecah (unpacking) ke dalam variabel count dan list_pemilik.
25. Mengecek apakah count lebih besar dari 0 (artinya data ditemukan).
26. Menampilkan pesan berapa kali nilai tersebut ditemukan.
27. Menampilkan daftar nama pemilik nilai. ' , '.join(list_pemilik) berfungsi menggabungkan list nama menjadi satu kalimat yang rapi dipisahkan koma.

28-29. Jika count adalah 0, tampilkan pesan bahwa nilai tidak ada di dalam data.
    
31-32. Blok except yang akan berjalan jika user salah memasukkan tipe data (misal input huruf saat diminta angka), sehingga program tidak langsung mati (force close).

Link : https://youtu.be/kzk5dQDpfHo
