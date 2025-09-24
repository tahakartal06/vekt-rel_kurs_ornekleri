girilen = input()
# girilen = input("Bir cümle giriniz:")


print("Girdiğiniz         : ",girilen)
print("Büyük harf şekli   : ",girilen.upper())
print("Küçük harf şekli   : ",girilen.lower())
print("İçindeki a nın yeri: ",girilen.find("a"))
print("İçindeki A sayısı1 : ",girilen.count("A"))
print("İçindeki A sayısı2 : ",girilen.upper().count("A"))
print("a ları _ yap       : ",girilen.replace("a","_"))
print("A ları _ yap       : ",girilen.upper().replace("A","_"))
