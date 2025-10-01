

# sınıf veri kalıbı yada veri tipidir.
class Ogrenci():
    adi = "---" # atribute/özellikleri/property
    numarasi = 0
    # ...


# aa2 = Ogrenci() # aa2 Ogrenci türü bir object tir. Yani nesne
# print(type(aa2))
# print(aa2.adi)


# aa3 = Ogrenci()
# print(aa3.adi)


# aa2.adi = "Volkan"
# aa3.adi = "Arda"
# print(aa2.adi)
# print(aa3.adi)
# print(aa3.numarasi)


# her nesnenin özellikleri/property ve metodları/fonksiyon/işlevi olur


class Ogretmen():
    # adi = "tanimsiz"
    # tc = "---"
    # brans = "brans yok"
    # siniflari = []
    def __init__(self,a="tanimsiz",b="---",c="brans yok",d=[]):
        self.adi = a
        self.tc = b
        self.brans = c
        self.siniflari = d


ogretmen1 = Ogretmen("Taha","512312312312341","Fizik",["10A","10B"])
ogretmen2 = Ogretmen()
ogretmen3 = Ogretmen()
ogretmen4 = Ogretmen()


# ogretmen1.adi = "Melikşah"
# ogretmen1.brans = "Fizik"
# ogretmen1.siniflari = ["10A","10B"]


print(ogretmen1.adi)
print(ogretmen2.adi)
print(ogretmen1.siniflari)