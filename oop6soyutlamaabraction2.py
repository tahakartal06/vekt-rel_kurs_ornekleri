from abc import ABC, abstractmethod


class KocPersonel(ABC):
    def __init__(self,tc,ad,brm):
        self.TC = tc
        self.adi = ad
        self.birim = brm
        self.maasi = 0
        print("\nPersonel oluştu")


    def personelBilgi(ss):
        return f"\n\nPersonel Bilgisi:\nTC :\t{ss.TC}\nAdı:\t{ss.adi}\nBirimi:\t{ss.birim}\nMaşı:\t{ss.maasi}"
   
    @abstractmethod
    def maasCizelgesi(self): pass


    @abstractmethod
    def izinCizelgesi(self): pass




class YapiKrediPersonel(KocPersonel):
    def __init__(self, tc, ad):
        super().__init__(tc, ad, "Yapı kredi")
        self.maasCizelgesi()
        print("\nYapı kredi personeli oluştu.")


    def maasCizelgesi(self):
        self.maasi = 50000
        print("Yapı kredi personeli maaş çizelgesi oluştu.")
   
    def izinCizelgesi(self):
        print("Yapı kredi personeli izin çizelgesi oluştu.")


class BekoPersonel(KocPersonel):
    def __init__(self, tc, ad):
        super().__init__(tc, ad, "Beko")
        self.maasCizelgesi()
        print("\nBeko personeli oluştu.")


    def maasCizelgesi(self):
        self.maasi=40000
        print("Beko personeli maaş çizelgesi oluştu.")
   
    def izinCizelgesi(self):
        print("Beko personeli izin çizelgesi oluştu.")


p1 = YapiKrediPersonel(233423455672,"Arda Güler")
p2 = BekoPersonel(85748521548,"Levent Karaca")
p3 = BekoPersonel(25685744776,"Melik Gazi")


print(p1.personelBilgi())
print(p3.personelBilgi())
