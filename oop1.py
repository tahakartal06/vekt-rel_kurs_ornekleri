class Ogrenci():
    ad = "---"
    numara = 0

ogrenci1 = Ogrenci()

print(ogrenci1.ad)
ogrenci1.ad = "Melikşah"
print(ogrenci1.ad)

ogrenci2 = Ogrenci()
print(ogrenci2.numara)
print(ogrenci2.ad)

ogrenci3 = Ogrenci()
ogrenci3.ad = "taha"
ogrenci3.numara = 5789438912
print(ogrenci3.ad , ogrenci3.numara)

print(type(ogrenci2))

class Magaza():
    adı = "___"
    şubesi = "___"
    adresi = "___"
    iletişimno = 0
    konsepti = "___"

magaza1 = Magaza()
magaza1.adı = "apple"
magaza1.şubesi = "haymana"
magaza1.iletişimno = 8712392133
magaza1.konsepti = "elektronik"

print(magaza1.adı , magaza1.adresi)
print(magaza1.iletişimno , magaza1.konsepti)

