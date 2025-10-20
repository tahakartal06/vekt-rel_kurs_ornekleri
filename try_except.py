try:
    print(10/0)
except Exception as xx:
    print("Hata oluştu:", xx)
except ZeroDivisionError:
    print("Sayı sıfıra bölünemez")
except TypeError:
    print("Yanlış değer girilmiş")