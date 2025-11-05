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
    secilen1.execute("CREATE DATABASE IF NOT EXISTS ots")
    secilen1.execute("CREATE TABLE IF NOT EXISTS rehber(id int, ad varchar(50), numara varchar(11))")

except Exception as hata:
    print("veritabanına bağlanırken bir hata oluştu:")
    print(hata)