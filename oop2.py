class Magaza():
    def __init__(self,a,n,b,s,t):
        self.adı=a
        self.şubesi=n
        self.adresi=b
        self.iletişimno=s
        self.konsepti=t
    def bilgi_ver(xx):
        return f"\n\nMağaza Bilgileri:\nAd: {xx.adı}, \nŞubesi: {xx.şubesi}, \nAdresi:{xx.adresi}, \nİletişim Numarası:{xx.iletişimno}"

magaza1 = Magaza("taha","balgat","____",1412412415,"bilgisayar")
magaza2 = Magaza("kartal","keçiören","ıjaskdasdasdasd",95345435435,"tekstil")


print(magaza1.bilgi_ver())
print(magaza2.bilgi_ver())