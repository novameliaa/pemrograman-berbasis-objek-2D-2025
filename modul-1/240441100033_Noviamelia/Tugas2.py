class Mahasiswa:
    def __init__(self, nama, nim, jurusan, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.prodi = prodi
        self.alamat = alamat
    
    def tampilkan_info(self):
        print("Data Mahasiswa:")
        print(f"Nama       : {self.nama}")
        print(f"NIM        : {self.nim}")
        print(f"Jurusan    : {self.jurusan}")
        print(f"Prodi      : {self.prodi}")
        print(f"Alamat     : {self.alamat}")

mahasiswa_list = []

for i in range(3):
    print(f"Masukkan data mahasiswa {i+1}:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    jurusan = input("Jurusan: ")
    prodi = input("Prodi: ")
    alamat = input("Alamat: ")
    
    mahasiswa = Mahasiswa(nama, nim, jurusan, prodi, alamat)
    mahasiswa_list.append(mahasiswa)

print("=========================")
print("   Data Mahasiswa   ")
print("=========================")
for mhs in mahasiswa_list:
    mhs.tampilkan_info()
    print("-------------------------")
