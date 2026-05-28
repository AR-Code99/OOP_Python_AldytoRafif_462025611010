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

class CustomerTetap:
    def produk_yg_diminati(self):
        print(f"jika customer memesan lebih dari 10 kali, maka ia adalah customer tetap.")

def data_customer(customer):
    customer.produk_yg_diminati()


freelancer = Customer("Budi")
karyawan = Designer("Vian")
developer = Programmer("Dyto")
customer_tetap = CustomerTetap()

print("--- MINAT PRODUK ---")
data_customer(freelancer)   
data_customer(karyawan)         
data_customer(developer)
#duck typing
print("-- syarat customer tetap --") 
data_customer(customer_tetap)