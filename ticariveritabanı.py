# pyqt ile veritabanına ulaşma
# pip install mysql-connector-python
import mysql.connector
try:
  veritabani1 = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
  )
  secilen1 = veritabani1.cursor()
  secilen1.execute("CREATE DATABASE IF NOT EXISTS ticarivt")
  secilen1.execute("show databases")
  vt_listesi = secilen1.fetchall()
  print("\n\nVeritabanı oluştu;\n",vt_listesi)


  secilen1.execute("CREATE TABLE IF NOT EXISTS ticarivt.kullanicilar(id int AUTO_INCREMENT PRIMARY KEY, ka VARCHAR(30), sf VARCHAR(20))")
  secilen1.execute("CREATE TABLE IF NOT EXISTS ticarivt.stoklar(id int AUTO_INCREMENT PRIMARY KEY, stokadi VARCHAR(30), stokmiktari int)")
  secilen1.execute("INSERT INTO ticarivt.kullanicilar (ka, sf) VALUES ('adm', '123')")


  veritabani1.commit()  # kayıt ekleme ve düzenleme için lazım.
  print(secilen1.rowcount, "kayıt eklendi.")


  kayitlar = secilen1.execute("SELECT * FROM ticarivt.kullanicilar")
  kayitlar = secilen1.fetchall() # commit olmadan ekleme, silme ve değişikli veri tabanına işlenmez.
  print(kayitlar)
  print("işlem tamam.")


except Exception as hata:
  print("Bir hata oluştu.")
  print(hata)
