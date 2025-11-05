import mysql.connector

try:
  veritabani1 = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="1234", 
    database="ots" 
  )
  secilen1 = veritabani1.cursor()
  
  komut = "SELECT * FROM rehber WHERE ad = %s"
 
  xx = input("Aradığınız kayıt: ")
  aranan = (xx,) 

  secilen1.execute(komut, aranan)
  kayitlistesi = secilen1.fetchall() 
  print(*kayitlistesi, sep="\n")
  print("işlem tamam.")


except Exception as hata:
  print("Veritabanına bağlanırken bir hata oluştu.")
  print(hata)
