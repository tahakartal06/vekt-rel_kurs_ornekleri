import re
def kontrol():
    ifade = input("Metin giriniz: ")
    desen = r"^sayın: [a-z]{9}"

    if re.fullmatch(desen, ifade):
        print("GEÇERLİ")
    else:
        print("GEÇERSİZ METİN")
    kontrol()

kontrol()