# OOP_Python_AldytoRafif_462025611010
# Sistem Pengauditan Barang Inventaris

Aplikasi ini adalah program berbasis Command Line Interface (CLI) untuk manajemen inventaris barang. Program ini mengimplementasikan konsep Object-Oriented Programming (OOP) secara menyeluruh menggunakan bahasa pemrograman Python.

## Fitur Utama

* Sistem Autentikasi: Terdapat fitur keamanan berupa login akun untuk admin menggunakan verifikasi username dan password.


* Manajemen Kategori Barang: Mendukung pencatatan input data untuk tiga kategori barang dengan spesifikasi unik: Elektronik, Non-Elektronik, dan Kendaraan.


* Penyimpanan data (I/O): Data barang disimpan dan dimuat secara otomatis menggunakan file eksternal data_inventaris.csv sehingga data tidak hilang setelah program ditutup.


* Validasi Input yang Kuat: Dilengkapi dengan penanganan error (Exception Handling) untuk mencegah program berhenti mendadak saat pengguna memasukkan tipe data yang salah (seperti huruf pada kolom angka) atau jumlah barang negatif.


* Pelaporan Sesi Dinamis: Menampilkan rekapitulasi keseluruhan daftar barang terbaru yang berhasil ditambahkan khusus pada sesi penggunaan tersebut di akhir program.



## Cara Menjalankan Program

Aplikasi ini tidak memerlukan instalasi library eksternal tambahan karena menggunakan module bawaan Python.

1. Buka terminal atau command prompt, lalu navigasikan ke dalam folder Final_Project.
2. Jalankan file utama aplikasi dengan mengetik: python UAS1.py
3. Saat layar login muncul, silakan masuk menggunakan kredensial bawaan sistem:

* Username: admin
* Password: password123

4. Ikuti menu interaktif yang muncul di terminal untuk mulai melakukan audit dan input barang.



## Penjabaran Konsep OOP yang Diterapkan

* Encapsulation: Status ketersediaan barang dan password admin dilindungi menggunakan atribut private(seperti self.__status) dan hanya dikontrol menggunakan metode getter dan setter khusus.


* Inheritance: Class BarangElektronik, BarangNonElektronik, dan Kendaraan diciptakan secara efisien dengan mewarisi atribut dari parent class utama yaitu Barang.


* Polymorphism: Masing-masing child class menggunakan konsep method overriding pada pemanggilan data sehingga format informasi akhir yang ditampilkan dapat beradaptasi sesuai dengan kategori barangnya.


* Magic Methods: Menggunakan dunder method __init__ sebagai konstruktor inisialisasi objek dan __str__ untuk merapikan hasil cetakan objek ke terminal.


* Advanced Methods (Static Method): Memanfaatkan @staticmethod pada modul utilitas seperti fungsi validasi jumlah barang dan pengelolaan baca-tulis file CSV yang tidak terikat langsung pada suatu instance objek.


* Robustness (Custom Exception): Menciptakan class error mandiri yaitu JumlahInvalidError khusus untuk menangkap pelanggaran logika bisnis aplikasi jika jumlah barang kurang dari nol.
