#Hesap Makinesi

def topla(a,b):
    return a+b
def carp(a,b):
    return a*b
def cikar(a,b):
    return a-b
def böl(a,b):
    return a//b


s1 = int(input("1.Sayıyı Giriniz:"))
s2 = int(input("2.Sayıyı Giriniz:"))
islem = input("İsleminiz Nedir(+,-,*,/)?")

if islem == "+" : print("Sonuç:", topla(s1,s2))
if islem == "*" : print("Sonuç:", carp(s1,s2))
if islem == "-" : print("Sonuç:", cikar(s1,s2))
if islem == "/" : print("Sonuç:", böl(s1,s2))
