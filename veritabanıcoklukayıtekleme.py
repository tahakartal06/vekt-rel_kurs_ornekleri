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
    a= "INSERT INTO rehber (ad,numara) VALUES (%s , %s)"

    b=[("Arda güler" , "12414141"),
       ("Erdinç Döner" , "5345435435"),
       ("Levent Akyol" , "324324224"),]
    
    secilen1.executemany(a, b)

    veritabanı1.commit()
    print(secilen1.rowcount, "kayıt eklendi.")


except Exception as hata:
    print("veritabanına bağlanırken bir hata oluştu:")
    print(hata)