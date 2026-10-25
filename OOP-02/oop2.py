class Perpustakaan:
    def __init__(self, nama, jumlah_buku):
        self.nama = nama
        self.jumlah_buku = jumlah_buku

    def pinjam_buku(self):
        if self.jumlah_buku > 0:
            self.jumlah_buku -= 1
            print("Buku berhasil dipinjam.")
        else:
            print("Maaf, stok buku sedang habis.")

    def kembalikan_buku(self):
        self.jumlah_buku += 1
        print("Buku berhasil dikembalikan.")

    def info_perpustakaan(self):
        print(f"Perpustakaan: {self.nama}")
        print(f"Buku tersedia: {self.jumlah_buku}")


perpus = Perpustakaan("Perpustakaan Sekolah", 5)
perpus.info_perpustakaan()
perpus.pinjam_buku()
perpus.info_perpustakaan()
perpus.kembalikan_buku()
perpus.info_perpustakaan()
