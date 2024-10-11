nama = input("masukan sebuah nama : ")
print(nama, "Hai sayang aku zulfa")
nama = input("apakah kamu suka aku ? (y/n) :").lower() == 'y'
print("wah sosweet❤️❤️❤️❤️❤️")
nama = input("apakah kamu sudah makan ? (y/n) :").lower() == 'y'
print("oh sudah")
nama = input("maukah kamu berhitung dengan ku (y/n) :").lower() =='y'
print("Mari kita berhitung ")
num1 = int(input("masukan angka terbaik mu sayang:"))
operator = input("Masukan operator yang kamu mau (+, -, *) : ")
num2 = int(input("masukan lagi satu lagi :"))
if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
else :
    print("ayo donh sekali saja")