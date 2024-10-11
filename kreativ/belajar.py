class Kalkulator :
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def tambah(self):
        return self.num1 + self.num2

    def kurang(self):
        return self.num1 - self.num2

    def kali(self):
        return self.num1 * self.num2

    def bagi(self):
       if self.num2 == 0:
        return "Tidak bisa melakukan pembagian"

       else:
        return self.num1 / self.num2

num1 = int(input("Masukan angka 1: "))
num2 = int(input("Masukan angka 2: "))


cal = Kalkulator(num1, num2)

print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilih = input ("Masukan pilihan operasi(1/2/3/4) : ")

if pilih == "1":
    print ("Hasil :" , cal.tambah())
elif pilih == "2":
    print ("Hasil :" , cal.kurang())
elif pilih == "3":
    print ("Hasil :" , cal.kali())
elif pilih == "4":
    print ("Hasil :" , cal.bagi())
else:
    print ("Masukan pilihan yang benar")
