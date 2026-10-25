class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(f"{self.nama} mulai berlari.")

    def ambil_koin(self, jumlah):
        self.koin += jumlah
        print(f"{self.nama} mengambil {jumlah} koin. Total koin: {self.koin}")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"{self.nama} menabrak rintangan. Game over!")

    def info_player(self):
        status = "Sedang berlari" if self.is_running else "Berhenti"
        print(f"Nama: {self.nama}")
        print(f"Skor: {self.skor}")
        print(f"Koin: {self.koin}")
        print(f"Status: {status}")


player1 = KarakterSurfer("Jake")
player1.info_player()
player1.ambil_koin(5)
player1.tabrak_rintangan()
player1.info_player()
