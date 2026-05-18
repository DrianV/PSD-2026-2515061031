def main():
    antrian_pijat = []
    BATAS_MAKSIMAL = 5
    
    while True:
        sisa_kuota = BATAS_MAKSIMAL - len(antrian_pijat)
        print(f"\n=== ANTRIAN PIJAT FULL BADAN PANGGILAN ===")
        print(f"Slot Tersedia Hari Ini: {sisa_kuota} orang")
        print("1. Booking Antrian (Tambah)")
        print("2. Panggil Pelanggan Berikutnya (Layani)")
        print("3. Lihat Daftar Antrian")
        print("4. Selesai / Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            if len(antrian_pijat) >= BATAS_MAKSIMAL:
                print("Maaf, kuota pijat panggilan hari ini sudah penuh (Maks 5 orang)!")
            else:
                nama = input("Masukkan nama pelanggan: ")
                if nama.strip():
                    antrian_pijat.append(nama)
                    print(f"{nama} berhasil masuk daftar antrian nomor {len(antrian_pijat)}.")
                else:
                    print("Nama tidak boleh kosong!")
                    
        elif pilihan == "2":
            if len(antrian_pijat) == 0:
                print("📭 Antrian kosong, belum ada pelanggan yang booking.")
            else:
                pelanggan = antrian_pijat.pop(0)
                print(f"Terapis meluncur! Pelanggan '{pelanggan}' sedang dilayani untuk pijat full badan.")
                
        elif pilihan == "3":
            if len(antrian_pijat) == 0:
                print("Tidak ada pelanggan di dalam antrian saat ini.")
            else:
                print("\n📋 URUTAN ANTRIAN SAAT INI:")
                for urutan, nama in enumerate(antrian_pijat, 1):
                    print(f"{urutan}. {nama}")
                    
        elif pilihan == "4":
            print("Program selesai. Selamat beristirahat!")
            break
        else:
            print("Pilihan tidak valid! Masukkan angka 1-4.")

if __name__ == "__main__":
    main()