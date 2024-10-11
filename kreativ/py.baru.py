def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

def main():
    panjang = int(input("Masukkan panjang persegi panjang: "))
    lebar = int(input("Masukkan lebar persegi panjang: "))

    hasil = hitung_luas_persegi_panjang(panjang, lebar)

    print("Luas persegi panjang dengan panjang {} dan lebar {} adalah: {}".format(panjang, lebar, hasil))

if __name__ == "__main__":
    main()
