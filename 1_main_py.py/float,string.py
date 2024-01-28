#input integer dan kalkulator sedrhana
num1 = int(input("Masukan angka pertama :"))
num2 = int(input("Masukan angka kedua :"))
result = num1 + num2
result_1 = num1 * num2
result_2 = num1 - num2
result_3 = num1 / num2 
result_4 = num1 % num2
print ("Hasil penjumlahan :", result)
print("")
print("")
print ("Hasil penjumlahan :", result_1)
print("")
print("")
print ("Hasil penjumlahan :", result_2)
print("")
print("")
print ("Hasil penjumlahan :", result_3)
print("")
print("")
print ("Hasil penjumlahan :", result_4)

#kalkualtor kuadrat 
print("")
print("===============================")
print("")
num = float(input("masukan sebuah angka :"))
square = num ** 2
print("kuadrat :", square)

#penggunaan fungsi"input()" untuk string;"
print("")
print("===============================")
print("")
name = input("Masukan nama anda : ")
print("Halo, " + name + "!")



#kalkulator pangkat 
print("")
print("===============================")
print("")
base = float(input("Masukan angka dasar :"))
exponent = float(input("Masukan pangkat :"))
result - base ** exponent
print("Hasil pangkat : ", result)


#penggunaan "format()" untuk string formatting:
print("")
print("===============================")
print("")
age = int(input("Berapa usia anda ? "))
print("saya berusia {} tahun .", format(age))




#kalkulator pembagian dengan pembulatan 
print("")
print("===============================")
print("")
num1 = float(input("Masukan angka pertama :"))
num2 = float(input("masukan angka kedua :"))
result = round (num1 / num2, 2)
print("Hasil pembagian :", result)



#penggunaan "input()" untuk boolean:
print("")
print("===============================")
print("")
is_student = input("Apakah anda seorang siswa? (y/n) : ").lower() == 'y'
print("Status siswa :", is_student)



#kalkulator presentase 
print("")
print("===============================")
print("")
total = float(input("Masukam total nilai :"))
precentage = float(input("Masukan presenyase yang diinginkan :"))
result = (precentage / 100) * total
print("Nilai presentase : ", result)




