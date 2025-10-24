class Musteri:
    def __init__(self,aa,xx,yy):        
        self.TC = aa
        self.ad = xx
        self.hn = yy
        self.__bakiye = 0 # __ ile başlayan değişkenler kapsüllenir ve sınıf içerisinden değiştirilmesine izin verilir, dışarıda değişiklik yapılamaz.
    def paraYatir(s,ym,k=10):
        s.__bakiye += (ym-k)
        print(f"Yatırılan miktardan({ym}TL), {k}TL kadar komiyon kesildi. \nHesaptaki son durum: {s.__bakiye}")
    def bakiyeGoster(self):
        return self.__bakiye
    def hesapBilgisi(self):
        print (f"\n\nMusteri hesabı:\nTC: \t{self.TC}\nAdı:\t{self.ad}\nHespNo:\t{self.hn}\nBakiye:\t{self.__bakiye}")


musteri1 = Musteri(52632154872,"Mete",5566)
musteri2 = Musteri(52417451426,"Dila",8741)


musteri1.hesapBilgisi()
musteri2.hesapBilgisi()


musteri1.TC = 22334455664
musteri1.paraYatir(1000)
musteri1.paraYatir(2000)
musteri1.hesapBilgisi()

print("Müsteri bakiyesi:",musteri1.ad)
print("Müsteri bakiyesi:",musteri1.bakiyeGoster())