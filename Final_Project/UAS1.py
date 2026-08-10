import csv
import os

class JumlahInvalidError(Exception):
    pass

class FileHelper:
    file_name = "data_inventaris.csv"

    @staticmethod
    def simpan_ke_csv(daftar_barang):
        with open(FileHelper.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Kategori", "ID", "Nama", "Jumlah", "Status", "Ekstra"])
            
            for barang in daftar_barang:
                if isinstance(barang, BarangElektronik):
                    writer.writerow(["Elektronik", barang.id_barang, barang.nama, barang.jumlah, barang.get_status(), barang.garansi_tahun])
                elif isinstance(barang, BarangNonElektronik):
                    writer.writerow(["Non-Elektronik", barang.id_barang, barang.nama, barang.jumlah, barang.get_status(), barang.kondisi])
                elif isinstance(barang, Kendaraan):
                    writer.writerow(["Kendaraan", barang.id_barang, barang.nama, barang.jumlah, barang.get_status(), barang.plat_nomor])

    @staticmethod
    def file_csv():
        daftar_sementara = []
        if os.path.exists(FileHelper.file_name):
            with open(FileHelper.file_name, mode='r') as file:
                reader = csv.reader(file)
                next(reader, None)
                
                for row in reader:
                    if not row: continue
                    
                    kategori, id_brg, nama, jumlah, status, ekstra = row
                    jumlah = int(jumlah)
                    
                    if kategori == "Elektronik":
                        daftar_sementara.append(BarangElektronik(id_brg, nama, jumlah, status, ekstra))
                    elif kategori == "Non-Elektronik":
                        daftar_sementara.append(BarangNonElektronik(id_brg, nama, jumlah, status, ekstra))
                    elif kategori == "Kendaraan":
                        daftar_sementara.append(Kendaraan(id_brg, nama, jumlah, status, ekstra))
                        
        return daftar_sementara

class Akun:
    def __init__(self, username, password):
        self.username = username
        self.__password = password 

    def cek_login(self, input_password):
        if self.__password == input_password:
            return True
        else:
            return False

class Barang:
    def __init__(self, id_barang, nama, jumlah, status):
        self.id_barang = id_barang
        self.nama = nama
        self.jumlah = jumlah
        self.__status = status 

    def get_status(self):
        return self.__status
    
    def set_status(self, status_baru):
        status_valid = ["tersedia", "rusak", "dipinjam"]
        if status_baru in status_valid:
            self.__status = status_baru
        else:
            print("Error: status tidak valid!")

    @staticmethod
    def validasi_jumlah(jumlah):
        if jumlah < 0:
            raise JumlahInvalidError("Error: jumlah barang tidak boleh negatif")
        return True

    def __str__(self):
        return f"({self.id_barang}) {self.nama} | Jumlah: {self.jumlah} | Status: {self.__status}"


class BarangElektronik(Barang):
    def __init__(self, id_barang, nama, jumlah, status, garansi_tahun):
        super().__init__(id_barang, nama, jumlah, status)
        self.garansi_tahun = garansi_tahun

    def __str__(self):
        return super().__str__() + f" | Garansi: {self.garansi_tahun} Tahun"

class BarangNonElektronik(Barang):
    def __init__(self, id_barang, nama, jumlah, status, kondisi):
        super().__init__(id_barang, nama, jumlah, status)
        self.kondisi = kondisi

    def __str__(self):
        return super().__str__() + f" | Kondisi: {self.kondisi}"

class Kendaraan(Barang):
    def __init__(self, id_barang, nama, jumlah, status, plat_nomor):
        super().__init__(id_barang, nama, jumlah, status)
        self.plat_nomor = plat_nomor 

    def __str__(self):
        return super().__str__() + f" | Plat No: {self.plat_nomor}"

daftar_terbaru = []

admin = Akun("admin", "password123")
daftar_inventaris = FileHelper.file_csv()

print("="*36)
print("SELAMAT DATANG DI SISTEM INVENTARIS")
print("="*36)

login_berhasil = False
while not login_berhasil:
    input_user = input("Username: ")
    input_pass = input("Password: ")
    
    if input_user == admin.username and admin.cek_login(input_pass):
        print("\nLogin Berhasil\n")
        login_berhasil = True
    else:
        print("Username atau Password salah, silakan coba lagi.\n")

print("SISTEM PENGAUDITAN BARANG INVENTARIS")

while True:
    print("\nPilih Kategori Barang:\n1. Barang Elektronik\n2. Barang Non-Elektronik\n3. Kendaraan\n4. Selesai & Tampilkan Hasil Audit")
    pilihan = input("Masukkan pilihan (1-4): ")
    
    if pilihan == "4":
        break
        
    if pilihan in ["1", "2", "3"]:
        print("\nInput Data Barang")
        kode = input("Masukkan Kode Barang: ")
        nama = input("Masukkan Nama Barang: ")

        
        try:
            jumlah = int(input("Masukkan Jumlah Barang: "))
            Barang.validasi_jumlah(jumlah)
        except ValueError:
            print("ERROR: Input jumlah harus berupa angka")
            continue
        except JumlahInvalidError as e:
            print(e)
            continue
            
        status = input("Masukkan Status Barang (tersedia/rusak/dipinjam): ")
        
        if pilihan == "1":
            garansi = input("Masukkan Masa Garansi (Tahun): ")
            barang_baru = BarangElektronik(kode, nama, jumlah, status, garansi)
            daftar_inventaris.append(barang_baru)
            daftar_terbaru.append(barang_baru)
            
        elif pilihan == "2":
            kondisi = input("Masukkan Kondisi barang: ")
            barang_baru = BarangNonElektronik(kode, nama, jumlah, status, kondisi)
            daftar_inventaris.append(barang_baru)
            daftar_terbaru.append(barang_baru)
            
        elif pilihan == "3":
            plat = input("Masukkan plat Nomor Kendaraan: ")
            barang_baru = Kendaraan(kode, nama, jumlah, status, plat)
            daftar_inventaris.append(barang_baru)
            daftar_terbaru.append(barang_baru)

        FileHelper.simpan_ke_csv(daftar_inventaris)    
        print("Barang berhasil disimpan ke sistem")
    else:
        print("ERROR: Pilihan tidak valid")

print("\nDAFTAR BARANG HASIL AUDIT")
print("="*100)

if len(daftar_terbaru) == 0:
    print("Tidak ada barang baru yang ditambahkan")
else:
    for barang in daftar_terbaru:
        print(barang)
print("="*100)