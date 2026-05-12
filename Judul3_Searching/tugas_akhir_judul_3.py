def sequential_search(list_nama, list_nilai, n, target):
    i, counter, pemilik = 0, 0, []
    while i < n:
        if list_nilai[i] == target:
            counter += 1
            pemilik.append(list_nama[i])
        i += 1
    return counter, pemilik

def main():
    nama_mhs, nilai_mhs = [], []

    try:
        jmlh_mhs = int(input("Masukkan jumlah mahasiswa: "))

        for i in range(jmlh_mhs):
            nama = input(f"Nama mahasiswa ke-{i+1}: ")
            nilai = float(input(f"Nilai {nama}: "))
            nama_mhs.append(nama)
            nilai_mhs.append(nilai)

        target = float(input("\nMasukkan nilai yang ingin dicari frekuensinya: "))
        count, list_pemilik = sequential_search(nama_mhs, nilai_mhs, len(nilai_mhs), target)

        if count > 0:
            print(f"\nNilai {target} ditemukan sebanyak {count} kali.")
            print(f"Pemilik nilai tersebut: {' , '.join(list_pemilik)}")
        else:
            print(f"\nNilai {target} tidak ditemukan dalam data.")

    except ValueError:
        print("Kesalahan: Pastikan Anda memasukkan angka untuk jumlah mahasiswa dan nilai!")

if __name__ == "__main__":
    main()