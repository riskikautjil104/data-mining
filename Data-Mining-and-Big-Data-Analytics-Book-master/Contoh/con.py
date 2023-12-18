# Inisialisasi data buku
buku = {
    "001": "logika Matematika",
    "002": "Kuasai Python",
    "003": "Logarithm & Program"
}

# Inisialisasi data anggota perpustakaan
anggota = {
    "158": "deya",
    "160": "fika",
    "156": "amel"
}

# Inisialisasi data peminjaman buku
peminjaman_buku = {}

# Fungsi untuk meminjam buku
def pinjam_buku():
    id_buku = input("Masukkan ID buku yang ingin dipinjam: ")

    if id_buku in buku.keys():
        id_anggota = input("Masukkan ID anggota perpustakaan: ")

        if id_anggota in anggota.keys():
            if id_buku not in peminjaman_buku.keys() or peminjaman_buku[id_buku] == "":
                peminjaman_buku[id_buku] = id_anggota
                print("Buku", buku[id_buku], "berhasil dipinjam oleh", anggota[id_anggota])
            else:
                print("Buku", buku[id_buku], "sedang dipinjam oleh", anggota[peminjaman_buku[id_buku]])
        else:
            print("Anggota perpustakaan dengan ID", id_anggota, "tidak ditemukan.")
    else:
        print("Buku dengan ID", id_buku, "tidak ditemukan.")

# Fungsi untuk mengembalikan buku
def kembalikan_buku():
    id_buku = input("Masukkan ID buku yang ingin dikembalikan: ")

    if id_buku in buku.keys():
        if id_buku in peminjaman_buku.keys() and peminjaman_buku[id_buku] != "":
            id_anggota = peminjaman_buku[id_buku]
            peminjaman_buku[id_buku] = ""
            print("Buku", buku[id_buku], "telah dikembalikan oleh", anggota[id_anggota])
        else:
            print("Buku", buku[id_buku], "tidak sedang dipinjam.")
    else:
        print("Buku dengan ID", id_buku, "tidak ditemukan.")

if __name__ == '__main__':
    while True:
        print("\nMenu:")
        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            pinjam_buku()
        elif pilihan == "2":
            kembalikan_buku()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
