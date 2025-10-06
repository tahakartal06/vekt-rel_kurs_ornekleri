if secim == "1":
    ad = input("Adınızı giriniz                 :")
    soyad = input("Soyadınızı giriniz           :")
    tel = input("Telefon numaranızı giriniz     :")

    try:
        d = open("rehber.txt","a")
        d.write(f"{ad}:{soyad}:{tel}\n")
    except:
        print(f"Bir hata oluştu.")

if secim == "2":
    d = open(rehber.txt)
    okunan = d.readlines()
    for satir in okunan:
        elemanlar = satir.split(":")
        print(f"{elemanlar[0]}{elemanlar[1]}{elemanlar[2]}")
