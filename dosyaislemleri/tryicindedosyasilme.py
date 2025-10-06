import os

for a in range(13):
    try:
        os.remove(f"dosyaislemleri/deneme{a}.txt")
    except:
        print(f"Bir hata oluştu Muhtemelen deneme {a}.txt dosyası yok.")