import mysql.connector
try:
    veritabanı1 = mysql.connector.connect(
        host="localhost",
        user= "root",
        password="1234",
        database="okul"
    )
    print("Bağlantı tamam:")
    secilen1 = veritabanı1.cursor()
    secilen1.execute("drop table okul.deneme.wb")


except Exception as hata:
    print("Bir hata oluştu:")
    print(hata)