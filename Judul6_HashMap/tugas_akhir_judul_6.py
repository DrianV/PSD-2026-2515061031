def tampilkan_semua_data(database_mahasiswa):
    print("\n--- DAFTAR MAHASISWA SAAT INI ---")
    if not database_mahasiswa:
        print("(Database kosong)")
    else:
        for npm, nama in database_mahasiswa.items():
            print(f"NPM: {npm} | Nama: {nama}")
    print("---------------------------------")

def cari_mahasiswa(database_mahasiswa):
    print("\n--- PENCARIAN DATA MAHASISWA ---")
    npm_dicari = input("Masukkan NPM yang dicari: ").strip()
    
    if npm_dicari in database_mahasiswa:
        print(f"--> Data ditemukan! Nama Mahasiswa: {database_mahasiswa[npm_dicari]}")
    else:
        print("--> Data mahasiswa tidak ditemukan!")

def tambah_mahasiswa(database_mahasiswa):
    print("\n--- TAMBAH DATA MAHASISWA BARU ---")
    npm_baru = input("Masukkan NPM Baru: ").strip()
    
    if not npm_baru:
        print("--> Gagal: NPM tidak boleh kosong!")
        return
    if npm_baru in database_mahasiswa:
        print(f"--> Gagal: NPM {npm_baru} sudah digunakan oleh {database_mahasiswa[npm_baru]}!")
    else:
        nama_baru = input("Masukkan Nama Mahasiswa: ").strip()
        if not nama_baru:
            print("--> Gagal: Nama tidak boleh kosong!")
            return
        database_mahasiswa[npm_baru] = nama_baru
        print(f"--> Sukses: Data {nama_baru} berhasil ditambahkan.")

def hapus_mahasiswa(database_mahasiswa):
    print("\n--- HAPUS DATA MAHASISWA ---")
    npm_hapus = input("Masukkan NPM yang ingin dihapus: ").strip()

    if npm_hapus in database_mahasiswa:
        nama_terhapus = database_mahasiswa.pop(npm_hapus)
        print(f"--> Sukses: Data mahasiswa dengan NPM {npm_hapus} ({nama_terhapus}) telah dihapus.")
    else:
        print("--> Data mahasiswa tidak ditemukan! Gagal menghapus.")

db_kampus = {
    "001": "Wira",
    "002": "Aldi",
    "003": "Andra"
}

while True:
    print("\n=================================")
    print("  SISTEM AKADEMIK KAMPUS (HASH)  ")
    print("=================================")
    print("1. Cari Mahasiswa (Berdasarkan NPM)")
    print("2. Tambah Mahasiswa Baru")
    print("3. Hapus Data Mahasiswa")
    print("4. Lihat Semua Data")
    print("5. Keluar")
    print("=================================")
    
    pilihan = input("Pilih menu (1-5): ").strip()
    
    if pilihan == "1":
        cari_mahasiswa(db_kampus)
    elif pilihan == "2":
        tambah_mahasiswa(db_kampus)
    elif pilihan == "3":
        hapus_mahasiswa(db_kampus)
    elif pilihan == "4":
        tampilkan_semua_data(db_kampus)
    elif pilihan == "5":
        print("\nTerima kasih! Program sistem akademik ditutup.")
        break
    else:
        print("\nPilihan tidak valid! Silakan masukkan angka 1 sampai 5.")