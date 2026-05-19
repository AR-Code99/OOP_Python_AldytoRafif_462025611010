class produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def info(self):
        print(f"ini adalah {self.nama} dengan harga {self.harga}")
        
    def jenis(self):
        print("produk ini memiliki jenis tertentu")

class baju(produk):
    def jenis(self):
        print("jenis baju: kaos, kemeja,dan jaket")
        super().jenis()

class celana(produk):
    def jenis(self):
        print("jenis celana: jeans, training, dan bahan")
        super().jenis()

class SatuPaket(baju, celana):
    def jenis(self):
        print("produk ini diskon jika dibeli satu paket, baju dan celana")
        super().jenis()

paket_produk = SatuPaket("UNIQLO", "500.000")
paket_produk.info()

print("jenis produk:")
paket_produk.jenis()

