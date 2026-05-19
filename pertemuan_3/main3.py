class Buku:
    Judul = ''
    Penulis = ''
    Bahasa = ''

    @staticmethod
    def status():
        print(f"Buku ini memiliki banyak peminat")
    def penulis(self):
        print("Buku dengan judul", self.Judul, "penulisnya adalah", self.Penulis)
    def bahasa(self):
        print(f'Buku dengan judul {self.Judul} menggunakan bahasa {self.Bahasa}')

buku1 = Buku()
buku1.Judul = 'negeri 5 menara'
buku1.Penulis = 'Ahmad Fuadi'
buku1.Bahasa = 'Indonesia'

buku1.status()
buku1.penulis() 
buku1.bahasa()

buku2 = Buku()
buku2.Judul = 'Laskar Pelangi'
buku2.Penulis = 'Andrea Hirata'
buku2.Bahasa = 'Indonesia'

buku2.status()
buku2.penulis()
buku2.bahasa()