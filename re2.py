import re 
def kontrol():
    telefon = input("Telefon numarası giriniz: ")

    desen = r"^0[5][0-9]{9}$"

    if re.fullmatch(desen, telefon):
        print("Telefon numarası geçerli.")
    else:
        print("Geçersiz telefon numarası.")
        print("11 haneli, 0 ile başlayan ve rakamlardan oluşan numara giriniz.")
    kontrol()


kontrol()