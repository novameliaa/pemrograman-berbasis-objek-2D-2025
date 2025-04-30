class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "truk":
            return 5
        elif self.jenis_kendaraan == "mobil":
            return 4
        else:
            return 6

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Wings Air":
            return 2
        elif self.maskapai == "Lion Air":
            return 3
        else:
            return 4

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)
        estimasi_awal = min(waktu_darat, waktu_udara)

        if self.tujuan.lower() not in ["surabaya", "bandung", "yogyakarta"]:
            return estimasi_awal + 3
        else:
            return estimasi_awal
        
    def info(self):
        print(f"Asal            : {self.asal}")
        print(f"Tujuan          : {self.tujuan}")
        print("-" * 15)
        print("Pengiriman Darat")
        print(f"Jenis Kendaraan : {self.jenis_kendaraan}")
        print("-" * 15)
        print("Pengiriman Udara")
        print(f"Maskapai        : {self.maskapai}")
        print("-" * 15)
        print("Estimasi Waktu")
        print(f"Estimasi Waktu  : {self.estimasi_waktu()} hari")

pengiriman1 = PengirimanInternasional("Surabaya", "Bandung", "mobil", "Lion Air")
pengiriman2 = PengirimanInternasional("Medan", "Singapura", "truk", "Wings Air")
pengiriman3 = PengirimanInternasional("Bali", "Thailand", "truk", "Garuda")
pengiriman4 = PengirimanInternasional("Yogyakarta", "Surabaya", "motor", "Wings Air")

print("=" * 40)
pengiriman1.info()
print("=" * 40)
pengiriman2.info()
print("=" * 40)
pengiriman3.info()
print("=" * 40)
pengiriman4.info()
print("=" * 40)
