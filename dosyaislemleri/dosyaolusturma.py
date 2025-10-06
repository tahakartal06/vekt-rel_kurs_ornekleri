dosya_sayisi = int(input("Kaç dosya oluşacak?"))

for a in range(dosya_sayisi):
    dosya = open(f"rehber{a}.txt","a")
    dosya.write(f"Bilgi{a}")