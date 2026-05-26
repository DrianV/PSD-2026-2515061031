class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def main(): 
    print("=== PROGRAM BINARY SEARCH TREE ===")
    while True:
        try:
            root_input = input("Masukkan nilai untuk ROOT (harus angka): ")
            root = Node(int(root_input))
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka bulat!")

    print(f"\nRoot {root.val} berhasil dibuat.")
    print("Silakan masukkan angka lain. Ketik 'selesai' jika sudah cukup.\n")

    while True:
        pilihan = input("Masukkan angka baru (atau ketik 'selesai'): ")
        if pilihan.strip().lower() == 'selesai':
            break
        try:
            nilai_baru = int(pilihan)
            insert(root, nilai_baru)
            print(f"-> Angka {nilai_baru} berhasil dimasukkan.")
        except ValueError:
            print("Input salah! Masukkan angka bulat atau ketik 'selesai'.")

    # 3. Menampilkan hasil akhir
    print("\n=========================================")
    print("Hasil Akhir Berurutan:")
    inorder(root)
    print("\n=========================================")
    print("Program selesai. Terima kasih!")

main()