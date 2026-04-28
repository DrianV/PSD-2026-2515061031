MAX_SLOT = 5
inventory = [None] * MAX_SLOT


def tampilkan_inventory():
    print("\n=== INVENTORY ===")
    for i, slot in enumerate(inventory):
        if slot is None:
            print(f"{i}. Kosong")
        else:
            print(f"{i}. {slot['nama']} x{slot['jumlah']}")
    print("=================\n")


def tambah_item():
    nama = input("Masukkan nama item: ")
    
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus angka!")
        return

    for slot in inventory:
        if slot is not None and slot["nama"].lower() == nama.lower():
            slot["jumlah"] += jumlah
            print(f"{nama} ditambahkan. Total sekarang: {slot['jumlah']}")
            return

    for i in range(len(inventory)):
        if inventory[i] is None:
            inventory[i] = {"nama": nama, "jumlah": jumlah}
            print(f"{nama} masuk ke slot {i}")
            return

    print("Inventory penuh!")


def hapus_item():
    tampilkan_inventory()
    
    print("Panduan hapus item")
    print("Masukkan nomor indeks sesuai slot item")

    try:
        indeks = int(input("Masukkan indeks item: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    if indeks < 0 or indeks >= len(inventory):
        print("Indeks tidak valid!")
        return

    if inventory[indeks] is None:
        print("Slot tersebut kosong!")
        return

    nama_item = inventory[indeks]["nama"]
    inventory[indeks] = None
    print(f"{nama_item} berhasil dihapus dari slot {indeks}")


while True:
    print("MENU INVENTORY")
    print("1. Lihat Inventory")
    print("2. Tambah Item")
    print("3. Hapus Item")
    print("4. Keluar")

    pilihan = input("Pilihan: ")

    if pilihan == "1":
        tampilkan_inventory()
    elif pilihan == "2":
        tambah_item()
    elif pilihan == "3":
        hapus_item()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")