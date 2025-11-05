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
    secilen1.execute("UPDATE rehber SET numara = '112113131' WHERE ad= 'kartal taha' ")

    veritabanı1.commit()
    print("işlem tamam:")
    

except Exception as hata:
    print("veritabanına bağlanırken bir hata oluştu:")
    print(hata)