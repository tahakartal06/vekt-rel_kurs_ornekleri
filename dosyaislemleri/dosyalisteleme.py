d = open("rehber.txt")
okunan = d.readlines()
for satir in okunan:
        elemanlar = satir.split(":")
        print(f"{elemanlar[0]}\t{elemanlar[1]}\t{elemanlar[2]}")
