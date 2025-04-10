class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} umur {self.umur} tahun dari {self.alamat} sedang berjalan.")
    
    def berlari(self):
        print(f"{self.nama} umur {self.umur} tahun dari {self.alamat}  sedang berlari.")

manusia1 = Manusia("Amel", 19, "Bangkalan")
manusia2 = Manusia("yanto", 24, "Bandung")
manusia3 = Manusia("yanti", 19, "Lamongan")
manusia4 = Manusia("Yuda", 24, "Lamongan")
manusia5 = Manusia("iky", 21, "Semarang")

manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()
