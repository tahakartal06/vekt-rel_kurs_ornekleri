class Ilan():
    def __init__(self,bb,nn):
        self.baslik = bb # prop/property/özellik
        self.no = nn # prop/property/özellik
    def bilgiVer(self): # sınıf metodu. kısaca method
        print("\n\nİlan Bilgileri")
        print("Başlık: \t\t",self.baslik)
        print("Numara: \t\t",self.no)


class Ev(Ilan):
    def __init__(self, xx, yy,m2,kat):
        super().__init__(xx, yy)
        self.metrekare = m2
        self.kati = kat


    def bilgiVer(self):
        super().bilgiVer()
        print("Metrekare: \t\t",self.metrekare)
        print("Bulunduğu kat: \t\t",self.kati)


# SatilikEv, KiralikEv ve Araba sınıflarını oluştur.
# bilgiVer metodlarını düzenle veya kendi metodlarını ekle.
# Bu sınıflardan nesne oluştur.
class KiralikEv(Ev):
    def __init__(aa, xx, yy, m2, kat, dep, kirasi):
        super().__init__(xx, yy, m2, kat)  
        aa.depozito = dep
        aa.kira = kirasi


    def bilgiVer(self):
        super().bilgiVer()
        print("Depozito: \t\t",self.depozito)
        print("Kirası: \t\t",self.kira)


class Arac(Ilan):
    def __init__(self, bb, nn, yil, marka):
        super().__init__(bb, nn)
        self.yili = yil
        self.markasi = marka
   
    def bilgiVer(self):
        super().bilgiVer()
        print("Markasi: \t\t",self.markasi)
        print("Yılı: \t\t",self.yili)  


ilan1 = Ilan("Acil satılık doğan görünümlü şahin", 444)
ilan2 = Ev("Acil satılık 4+1",333,150,3)


ilan1.bilgiVer()
ilan2.bilgiVer()


ev3 = KiralikEv("full yapılı kiralık",2341,120,2,20000,15000)
print("ev3 bilgisi:")
ev3.bilgiVer()


ilan3 = Arac("Kazasız yumurta kasa",12311,2010,"Hundai")
ilan4 = Arac("Corrolla efsana kasa",43211,2000,"Toyota")


ilan3.bilgiVer()