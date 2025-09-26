import random
sorular = ["\n\nIhlara vadisi hangi ilimizdedir?\nA) Ankara \nB) Kayseri \nC) Aksaray",
           "\n\nSuyun kaynama derecesi kaçtır?\nA) 100 derece \nB) 70 derece", 
           "\n\nAnkara'nın eski ismi nedir?\nA) Angara \nB) Ankyra",
           "\n\nİnternetin kurucusu kimdir?\nA) Tim Berners \nB) Elon Musk",
           ]

cevaplar = [""]

devam = "Evet"
while devam.upper() in ["E","EVET",""]:

    sorusayisi = len(sorular)-1
    print(f"Listede {len(sorular)} adet soru var.")
    sorulacaksoru = random.randint(0,sorusayisi)
    print(f"Soru: {sorular[sorulacaksoru]} \nCevabınız Nedir?")
    cevap = input()
    print(cevaplar[sorulacaksoru])
    if cevap == cevaplar[sorulacaksoru]:
        print("bildin")
    else: 
        print("bilemedin")
    devam = input("Devam edecek misin?")
    
         


