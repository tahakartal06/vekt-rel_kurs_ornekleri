
def topla(a,b):
    print("Topla:",a+b)
    print("İslem tamam.\n")

topla(1,2)
topla(4,7)
topla(3,9)


def selamla():
    print("Merhaba")
    print("Selam")

selamla()
selamla()
selamla()

def eslestir (a,b):
     ogrenciler=['ayse','ali','ahmet','mehmet']
     if a in ogrenciler :
      print ('baloda beraberiz')
         
     else: print("değiliz")

eslestir("ali","veli")

def topla(a,b):
    return f"Çarpım: {a*b}"

print(topla(2,3))
print(topla(4,3))
print(topla(2,7))


 #default varsayılan örneği

def topla(a=0,b=0):
   return a+b
print(topla(2))
print(topla())
print(topla(1,2))

for a in range(5): print(a)
for a in range(5,9): print(a)
for a in range(5,9): print("a")#String yazar a a a a 
for a in range(5,9,2): print(a) #2şer atlıyarak

for a in range(5,10,2):
  print("\nSayı")
  print(a)

  