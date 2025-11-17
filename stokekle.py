# stokekle.py
import mysql.connector
try:
  veritabani1 = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="ticarivt" # ots = okultakipsistemi
  )
  secilen1 = veritabani1.cursor()
  print("işlem tamam.")

except Exception as hata:
  print("Bir hata oluştu.")
  print(hata)

import sys
from PyQt6.QtWidgets import *

class StokEkleme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stok Ekeleme Ekranı")
        central_widget = QWidget()
        layout = QVBoxLayout()

        label_stokadi = QLabel("Stok Adı:")
        self.stokadi_input = QLineEdit()
        layout.addWidget(label_stokadi)
        layout.addWidget(self.stokadi_input)

        label_stokmiktari = QLabel("Stok Miktarı:")
        self.stokmiktari_input = QLineEdit()
        layout.addWidget(label_stokmiktari)
        layout.addWidget(self.stokmiktari_input)

        label_stokturu = QLabel("Stok Türü:")
        self.stokturu_input = QLineEdit()
        layout.addWidget(label_stokturu)
        layout.addWidget(self.stokturu_input)

        login_button = QPushButton("Stok Ekle")
        login_button.clicked.connect(self.kaydet)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def kaydet(self):

        komut = "INSERT INTO ticarivt.stoklar (stokadi, stokmiktari, tur) VALUES (%s, %s, %s)"
       
        ad = self.stokadi_input.text()
        miktar = self.stokmiktari_input.text()
        tur = self.stokturu_input.text()
        veri = (ad, miktar, tur)
        print(ad, miktar, tur)
       
        secilen1.execute(komut, veri)
        veritabani1.commit()  # kayıt ekleme ve düzenleme için lazım.
        print(secilen1.rowcount, "kayıt eklendi.")
       

def main():
    app = QApplication(sys.argv)
    window = StokEkleme()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()




