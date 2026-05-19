class Absensi:
    __nama = ''
    __nim = 0
    __pin = ''
    __status = ''

    def __init__(self, nama, nim, pin):
        self.__nama = nama
        self.__nim = nim
        self.__pin = pin
        self.__status = "Belum Absen" 

    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    def get_status(self):
        return self.__status

    def rekap_absen(self, pin_input):
        if pin_input != self.__pin:
            print("PIN salah! Absensi ditolak.")
            return
        self.__status = "Hadir"
        print(f"Absensi atas nama {self.__nama} berhasil dicatat!")
    
    def lapor_absen(self, pin_input):
        if pin_input != self.__pin:
            print("PIN salah! Tidak dapat melaporkan absensi.")
            return
        self.__status = "Sakit"
        print(f"Absensi atas nama {self.__nama} berhasil dilaporkan sakit")

absen1 = Absensi("Aldyto Rafif", 462025611010, "123456")

# Pembuktian tidak dapat mengakses atribut privat langsung
# print(absen1.__pin) 
# program akan menghasilkan error: AttributeError: 'Absensi' object has no attribute '__pin'

absen1.rekap_absen("000000") #contoh kalo pin salah
absen1.rekap_absen("123456") #contoh kalo pin benar

print(f"Nama: {absen1.get_nama()}")
print(f"NIM: {absen1.get_nim()}")
print(f"Status: {absen1.get_status()}")

absen2 = Absensi("fulan", 462025611011, "654321")

absen2.lapor_absen("123456") 
print(f"Status: {absen2.get_status()}")

absen2.lapor_absen("654321")
print(f"Status: {absen2.get_status()}")