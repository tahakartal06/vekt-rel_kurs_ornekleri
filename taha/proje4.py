def proje4menü():
    print("╔"+"═"*30+"╗")
    print("║         Alan ve Çevre        ║")
    print("║                              ║")
    print("║        1-Alan ve Çevre(k)    ║")
    print("║        2-Alan ve Çevre(d)    ║")
    print("║        3-Alan ve Çevre()                      ║")
    print("║                              ║")
    print("║                              ║")
    print("║    Lütfen seçim yapınız :    ║")
    print("╚"+"═"*30+"╝")
    secim = input()
    if secim == "1" or secim == "k":
        import karealan
        karealan.karealanproje()
    if secim == "2" or secim == "d":
        import dikalancevre
        dikalancevre.dikalancevre()
if __name__ == "__main__":
    proje4menü()
   
