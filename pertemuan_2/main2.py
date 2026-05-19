class handphone:
    
    def __init__(self, merek, harga, spek):
        self.merek = merek
        self.harga = harga
        self.spek = spek

handphoneZidan = handphone("poco", "3.000.000", "8GB/256GB")
handphoneRafael = handphone("samsung", "15.000.000", "16GB/512GB")
handphoneDyto = handphone("iphone", "20.000.000", "16GB/1TB")

print(f"handphone Zidan: Merk {handphoneZidan.merek}, Harga {handphoneZidan.harga}, Spek {handphoneZidan.spek}")
print(f"handphone Rafael: Merk {handphoneRafael.merek}, Harga {handphoneRafael.harga}, Spek {handphoneRafael.spek}")
print(f"handphone Dyto: Merk {handphoneDyto.merek}, Harga {handphoneDyto.harga}, Spek {handphoneDyto.spek}")