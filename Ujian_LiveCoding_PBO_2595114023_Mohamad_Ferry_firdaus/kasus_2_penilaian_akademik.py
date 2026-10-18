class PenilaianMahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama

        if not all(0 <=nilai <=100 for nilai in[tugas, uts, uas]):
            raise ValueError("nilai harus 0 sampai 100")

        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def hitung_nilai_akhir(self):
        return(self.tugas*0.30)+(self.uts*0.30)+(self.uas*0.40)

    def tentukan_grade(self):
        nilai=self.hitung_nilai_akhir()
        if nilai >=85:
            return "A"
        elif nilai >=75:
            return "B"
        elif nilai >=65:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"

    def tentukan_status(self):
        if self.hitung_nilai_akhir()>=65:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def tampilkan_hasil(self):
        print("\n=====HASIL AKADEMIK======")
        print(f"NIM : {self.nim}")
        print(f"NAMA : {self.nama}")
        print(f"NILAI AKHIR : {self.hitung_nilai_akhir():.2f}")
        print(f"GRADE : {self.tentukan_grade()}")
        print(f"STATUS : {self.tentukan_status()}")
        print("===========================")

try:
    nim= input("nim:")
    nama= input("nama: ")
    tugas= float(input("nilai tugas:"))
    uts= float (input("nilai uts:"))
    uas= float (input("nilai uas:"))

    mahasiswa= PenilaianMahasiswa(nim, nama, tugas, uts, uas)
    mahasiswa.tampilkan_hasil()
except ValueError as e:
    print("input tidak valid", e)