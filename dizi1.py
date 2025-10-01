# Pythonda 4 tür dizi vardır. Bunlara collection denir.
aa1 = [1,"Muz",True]#List
aa2 = (1,"Muz",True)#Tuple
aa3 = {"Cumartesi","Pazar"}#Set küme index ifadesi yoktur.
aa4 = {"calisma_gunleri":["Pt",'''Sl''','''Çr''',"Pr","Cu"],
       "tatil_gunleri":("Ct","Pz")

}#dictionary sözlük key ve value

aa5 = 4 #aa5 int türü bir object tir yani nesne
aa6 = "Ankara"

print(aa1)
print(aa2)
print(aa3)
print(aa4)

aa1.append("---")
print(aa1)

print(type(aa6))
print(type(aa5))

# print("----------------\n",dir(aa5))
bb1 = aa6.upper()
# def upper(): fonksiyonlar sınıf içerisinde kalınca metod olarak adlandırılırlar.
#     ...
print(bb1)