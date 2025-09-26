def topla():
    print("toplama işlemi yapıldı")
def cikar():
    print("cikarma işlemi yapıldı")
def böl():
    print("bölme işlemi yapıldı")
def carp():
    print("carpma işlemi yapıldı")
def proje2menu():
    print("╔"+"═"*30+"╗")
    print("║         Hesap Makinesi       ║")
    print("║                              ║")
    print("║        1-Toplama             ║")
    print("║        2-Çıkarma             ║")
    print("║        3-Bölme               ║")
    print("║        4-Çarpma              ║")
    print("║                              ║")
    print("║    Lütfen seçim yapınız :)   ║")
    print("╚"+"═"*30+"╝")
    secim = input()

    if secim == "1":
        
        import denemehesapmakinesi
        denemehesapmakinesi.topla()
    if secim == "2":
        import denemehesapmakinesi
        denemehesapmakinesi.carp()
    if secim == "3":
        import denemehesapmakinesi
        denemehesapmakinesi.böl()
    if secim == "4":
        import denemehesapmakinesi
        denemehesapmakinesi.cikar()
        
    




