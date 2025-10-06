d = open("rehber.txt","r")
okunan = d.readlines()
# print(okunan)
aranan = input("Aradığınız? : ")
bulunan = 0
for satir in okunan:
    # print(satir)
    # print(satir[:len(satir)-1])
    # print(len(satir))
    # elemanlar=satir.split("#")
    elemanlar=satir[:len(satir)-1].split("#")
    # print(elemanlar)
    if aranan in elemanlar:
        print(f"\n{elemanlar[0]}\t| {elemanlar[1]}\t| {elemanlar[2]}",end="")
        bulunan+=1


if bulunan==0:
    print(f"\nAranan '{aranan}' bulunamadı.")
else:
    print(f"\n{bulunan} adet '{aranan}' bulundu.")