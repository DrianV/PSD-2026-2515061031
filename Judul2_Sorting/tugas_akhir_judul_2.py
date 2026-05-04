def bubble_sort_anime(daftar):
    n = len(daftar)
    for i in range(n):
        for j in range(0, n- 1):
            if daftar[j] > daftar[j+1]:
                daftar[j], daftar[j+1] = daftar[j+1], daftar[j]

# List kosong untuk menampung data
maraton_list = []

print("--- Program Input Maraton Anime ---")
try:
    jumlah_input = int(input("Berapa banyak anime yang ingin dimasukkan? "))

    for i in range(jumlah_input):
        print(f"\nData ke-{i+1}:")
        nama = input("Masukkan judul anime: ")
        episode = int(input(f"Masukkan jumlah episode {nama}: "))
        maraton_list.append([nama, episode])

    # Proses Pengurutan
    bubble_sort_anime(maraton_list)

    # Menampilkan Hasil
    print("\n" + "="*30)
    print("HASIL URUTAN (EPISODE TERSEDIKIT)")
    print("="*30) 

    for anime in maraton_list:
        print(f"- {anime[0]:<20} | {anime[1]} Episode")

except ValueError:
    print("\nKesalahan: Mohon masukkan angka yang valid untuk jumlah episode!")