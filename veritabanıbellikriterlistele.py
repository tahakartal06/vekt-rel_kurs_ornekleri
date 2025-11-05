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
    secilen1.execute("SELECT * FROM okul.rehber where ad LIKE '%z%' ")
    kayitlistesi = secilen1.fetchall()
    print(*kayitlistesi, sep="\n")
    print("İşlem tamam:")


except Exception as hata:
    print("veritabanına bağlanırken bir hata oluştu:")
    print(hata)                                                                                                        