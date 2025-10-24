class Ilan():
    def __init__(self,bb,nn):
        self.baslik = bb # prop/property/
        self.no = nn
    def bilgiVer(self):
        print("\n\nİlan Bilgileri")
        print("Başlık: \t\t",self.baslik)
        print("Numara: \t\t",self.no)


class Ev(Ilan):
    def __init__(self, bb, nn, m2, kat):
        super().__init__(bb, nn)
        self.metrekare = m2
        self.kati = kat


    def bilgiVer(self):
        super().bilgiVer()
        print("Metrekare: \t\t",self.metrekare)
        print("Bulunduğu kat: \t\t",self.kati)
class KiralikEv(Ev):
    def __init__(self, bb, nn, m2, kat, dep, kirasi):
        super().__init__(bb, nn, m2, kat)
        self.depozito =  dep
        self.kirasi = kirasi

    def bilgiVer(self):
        super().bilgiVer()
        print("Depozito: \t\t",self.depozito)
        print("Kirası: \t\t",self.kirasi)



ilan1 = Ilan("Acil satılık doğan görünümlü şahin", 444)
ilan2 = Ev("Acil satılık 4+1",333,150,3)


ilan1.bilgiVer()
ilan2.bilgiVer()

# ev3 = KiralıkEv("Full yapılı kiralık",123123,1237123,5345436,43543637,214)

# ev3.bilgiVer()
ev3 = KiralikEv("Kiralık ev",532,45,2,345,25000)
ev3.bilgiVer()