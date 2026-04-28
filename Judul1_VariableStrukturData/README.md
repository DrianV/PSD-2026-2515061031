Struktur Data List Dalam Program Inventory Barang

Deskripsi Singkat
Program ini berfungsi sebagai sistem manajemen inventaris sederhana yang memungkinkan pengguna mengelola penyimpanan barang dengan kapasitas terbatas (maksimal 5 slot). Program ini menerapkan struktur data List (Array) berukuran tetap yang menyimpan elemen untuk merepresentasikan detail barang (nama dan jumlah).

SOURCE CODE
 
 
MAX_SLOT = 5
inventory = [None] * MAX_SLOT
•	MAX_SLOT = 5 → menentukan kapasitas maksimum inventory. 
•	inventory = [None] * MAX_SLOT → membuat list berisi 5 slot kosong (None).


Fungsi tampilkan_inventory()
def tampilkan_inventory():
•	Mendefinisikan fungsi untuk menampilkan isi inventory. 
print("\n=== INVENTORY ===")
•	Menampilkan judul inventory. 
for i, slot in enumerate(inventory):
•	Melakukan iterasi list inventory. 
•	i = indeks, slot = isi slot. 
if slot is None:
    print(f"{i}. Kosong")
•	Jika slot kosong, tampilkan "Kosong". 
else:
    print(f"{i}. {slot['nama']} x{slot['jumlah']}")
•	Jika berisi item, tampilkan nama dan jumlah. 
print("=================\n")
•	Penutup tampilan inventory.


Fungsi tambah_item()
def tambah_item():
•	Fungsi untuk menambahkan item ke inventory. 
nama = input("Masukkan nama item: ")
•	Input nama item. 
try:
    jumlah = int(input("Masukkan jumlah: "))
•	Input jumlah item dan dikonversi ke integer. 
except ValueError:
    print("Jumlah harus angka!")
    return
•	Jika input bukan angka → tampilkan error dan keluar dari fungsi. 

Cek apakah item sudah ada
for slot in inventory:
•	Iterasi seluruh inventory. 
if slot is not None and slot["nama"].lower() == nama.lower():
•	Jika slot tidak kosong dan nama item sama (case insensitive). 
slot["jumlah"] += jumlah
•	Tambahkan jumlah ke item yang sudah ada. 
print(f"{nama} ditambahkan. Total sekarang: {slot['jumlah']}")
return
•	Tampilkan hasil dan hentikan fungsi.

Cari slot kosong jika item belum ada
for i in range(len(inventory)):
•	Iterasi berdasarkan indeks. 
if inventory[i] is None:
•	Jika menemukan slot kosong. 
inventory[i] = {"nama": nama, "jumlah": jumlah}
•	Simpan item dalam bentuk dictionary. 
print(f"{nama} masuk ke slot {i}")
return
•	Tampilkan posisi slot dan keluar dari fungsi. 
print("Inventory penuh!")
•	Jika tidak ada slot kosong → inventory penuh. 


Fungsi hapus_item()
def hapus_item():
•	Fungsi untuk menghapus item. 
tampilkan_inventory()
•	Menampilkan inventory terlebih dahulu. 
print("Panduan hapus item")
print("Masukkan nomor indeks sesuai slot item")
•	Memberikan instruksi ke user. 
try:
    indeks = int(input("Masukkan indeks item: "))
•	Input indeks slot. 
except ValueError:
    print("Input harus berupa angka!")
    return
•	Validasi input angka. 

Validasi indeks
if indeks < 0 or indeks >= len(inventory):
•	Cek apakah indeks di luar batas. 
print("Indeks tidak valid!")
return
•	Jika tidak valid → keluar. 
if inventory[indeks] is None:
•	Cek apakah slot kosong. 
print("Slot tersebut kosong!")
return
•	Jika kosong → tidak bisa dihapus. 
nama_item = inventory[indeks]["nama"]
•	Simpan nama item sebelum dihapus. 
inventory[indeks] = None
•	Hapus item (set ke None). 
print(f"{nama_item} berhasil dihapus dari slot {indeks}")
•	Tampilkan konfirmasi. 


Loop Utama (Menu)
while True:
•	Loop tak terbatas untuk menjalankan program. 
print("MENU INVENTORY")
print("1. Lihat Inventory")
print("2. Tambah Item")
print("3. Hapus Item")
print("4. Keluar")
•	Menampilkan menu pilihan. 
pilihan = input("Pilihan: ")
•	Input pilihan user. 

Percabangan menu
if pilihan == "1":
    tampilkan_inventory()
•	Menampilkan inventory. 
elif pilihan == "2":
    tambah_item()
•	Menambah item. 
elif pilihan == "3":
    hapus_item()
•	Menghapus item. 
elif pilihan == "4":
    print("Program selesai.")
    break
•	Keluar dari program. 
else:
    print("Pilihan tidak valid!")
•	Jika input tidak sesuai menu. 

 
OUTPUT CODE

1. Tampilan Awal Menu
Saat program dijalankan, sistem langsung menampilkan menu utama:
MENU INVENTORY
1. Lihat Inventory
2. Tambah Item
3. Hapus Item
4. Keluar
Kemudian user memasukkan:
Pilihan: 2
Artinya user memilih menu Tambah Item.

2. Menambahkan Item Pertama (Sword)
Program meminta input:
Masukkan nama item: Sword
Masukkan jumlah: 2
Output:
Sword masuk ke slot 0
Penjelasan:
•	Inventory masih kosong → slot pertama (index 0) digunakan. 
•	Item "Sword" dengan jumlah 2 disimpan di slot 0. 

3. Menambahkan Item Kedua (Potion)
Menu muncul lagi, user memilih:
Pilihan: 2
Input:
Masukkan nama item: Potion
Masukkan jumlah: 10
Output:
Potion masuk ke slot 1
Penjelasan:
•	Slot 0 sudah terisi (Sword). 
•	Slot kosong berikutnya adalah index 1 → Potion dimasukkan ke slot 1. 

4. Melihat Inventory
User memilih:
Pilihan: 1
Output:
=== INVENTORY ===
0. Sword x2
1. Potion x10
2. Kosong
3. Kosong
4. Kosong
=================
Penjelasan:
•	Slot 0 → berisi Sword (2) 
•	Slot 1 → berisi Potion (10) 
•	Slot 2–4 → masih kosong 

5. Memilih Menu Hapus Item
User memilih:
Pilihan: 3
Program menampilkan inventory lagi (sebagai referensi):
=== INVENTORY ===
0. Sword x2
1. Potion x10
2. Kosong
3. Kosong
4. Kosong
=================
Lalu muncul panduan:
Panduan hapus item
Masukkan nomor indeks sesuai slot item
User memasukkan:
Masukkan indeks item: 0
Output:
Sword berhasil dihapus dari slot 0
Penjelasan:
•	User memilih slot 0 
•	Item "Sword" dihapus → slot tersebut kembali menjadi kosong (None) 

6. Melihat Inventory Setelah Penghapusan
User memilih:
Pilihan: 1
Output:
=== INVENTORY ===
0. Kosong
1. Potion x10
2. Kosong
3. Kosong
4. Kosong
=================
Penjelasan:
•	Slot 0 → sekarang kosong (karena Sword sudah dihapus) 
•	Slot 1 → masih berisi Potion (10) 
•	Slot lainnya tetap kosong 

7. Keluar dari Program
User memilih:
Pilihan: 4
Output:
Program selesai.
Penjelasan:
•	Program keluar dari loop (while True) 
•	Eksekusi program berhenti

<img width="1398" height="1125" alt="Output" src="https://github.com/user-attachments/assets/621bb1a6-a586-45ea-9fab-35ff9af47e42" />
<img width="1902" height="4842" alt="Source Code" src="https://github.com/user-attachments/assets/8d6843a9-6a18-45fb-97da-3ab9418ab120" />



