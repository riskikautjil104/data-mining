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
            if id_buku not in peminjaman_buku.keys():
                peminjaman_buku[id_buku] = id_anggota
                print("Buku", buku[id_buku], "berhasil dipinjam oleh", anggota[id_anggota])
            else:
                print("Buku", buku[id_buku], "sedang dipinjam oleh", anggota[peminjaman_buku[id_buku]])
        else:
            print("Anggota perpustakaan dengan ID", id_anggota, "tidak ditemukan.")
    else:
        print("Buku dengan ID", id_buku, "tidak ditemukan.")

if __name__ == '__main__':
    pinjam_buku()