aa1 = "Ankara"
print(type(aa1))


# sınıf veri kalıbı yada veri tipidir.


class Ogrenci():
    adi = "---"
    numarasi = 0
    # ...


aa2 = Ogrenci() # aa2 Ogrenci türü bir object tir. Yani nesne
print(type(aa2))
print(aa2.adi)


aa3 = Ogrenci()
print(aa3.adi)


aa2.adi = "Volkan"
aa3.adi = "Arda"
print(aa2.adi)
print(aa3.adi)
print(aa3.numarasi)


# her nesnenin özellikleri/property ve metodları/fonksiyon/işlevi olur

