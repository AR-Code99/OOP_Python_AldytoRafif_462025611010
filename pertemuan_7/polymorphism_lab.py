class Customer:
    def __init__(self, nama: str):
        self.nama = nama

    def produk_yg_diminati(self):
        print(f"{self.nama} merupakan customer tetap yg meminati produk digital.")

class Designer(Customer):
    def produk_yg_diminati(self):
        print(f"{self.nama} adalah designer yg meminati produk dengan desain yg unik.")

class Programmer(Customer):
    def produk_yg_diminati(self):
        print(f"{self.nama} adalah programmer yg meminati software yg efisien.")

def data_costumer(customer):
    customer.produk_yg_diminati()


freelancer = Customer("Budi")
karyawan = Designer("Vian")
developer = Programmer("Dyto")

print("--- MINAT PRODUK ---")
data_costumer(freelancer)   
data_costumer(karyawan)         
data_costumer(developer)