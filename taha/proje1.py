def anamenu():

    print("╔"+"═"*30+"╗")
    print("║           Ana sayfa          ║")
    print("║                              ║")
    print("║        1-Hesap Makinesi      ║")
    print("║        2-Uygulamalar         ║")
    print("║        3-Alan Hesaplama      ║")
    print("║        4-Oyunlar             ║")
    print("║                              ║")
    print("║    Lütfen seçim yapınız :)   ║")
    print("╚"+"═"*30+"╝")
    secim = input()
    if secim == "1":
        import proje2
        proje2.proje2menu()
    if secim == "2":
        import proje3
        proje3.proje3()
    if secim == "3":
        import proje4
        proje4.proje4()
    if secim == "4":
        import proje5
        proje5.proje5()
    anamenu()

anamenu()


