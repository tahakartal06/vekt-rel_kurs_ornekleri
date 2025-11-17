# stokliste.py
import mysql.connector

def stoklari_al():
    baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
    secilen1 = baglanti.cursor()
    secilen1.execute("SELECT * FROM stoklar")
    stoklar = secilen1.fetchall()  # Liste olarak al
    baglanti.close()
    return stoklar

import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtWidgets import *

class StokTablosu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stok Listesi")
        self.setGeometry(100, 100, 500, 300)

        # Layout oluştur
        layout = QVBoxLayout()

        # QTableWidget oluştur (4 sütunlu)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "STOK ADI", "MİKTARI", "TÜRÜ"])
        self.tableWidget.cellClicked.connect(self.satir_tiklandi)

        # Verileri tabloya ekle
        # stoklar = [
        #     (1, "Ali Yılmaz", 20, "Bilgisayar Müh."),
        #     (2, "Ayşe Kaya", 22, "Makine Müh."),
        #     (3, "Mehmet Demir", 21, "Elektrik-Elektronik Müh."),
        #     (4, "Zeynep Arslan", 23, "İnşaat Müh.")
        # ]
        stoklar = stoklari_al()
        self.populate_table(stoklar)


        butonlarLayout = QVBoxLayout()
        silButonu = QPushButton("Sil")
        duzeltButonu = QPushButton("Düzenle")
        kaydetButonu = QPushButton("Ekle")
        butonlarLayout.addWidget(silButonu)
        butonlarLayout.addWidget(duzeltButonu)
        butonlarLayout.addWidget(kaydetButonu)

        silButonu.clicked.connect(self.kayitSilme)
        duzeltButonu.clicked.connect(self.kayitDuzenleme)
        kaydetButonu.clicked.connect(self.kayitEkle)
               
        kayitlarLayout = QHBoxLayout()
        adLayout = QVBoxLayout()
        mkLayout = QVBoxLayout()
        trLayout = QVBoxLayout()
       
        self.adtb = QLineEdit()
        self.miktartb = QLineEdit()
        self.turtb = QLineEdit()
        adLayout.addWidget(QLabel("Adı"))
        adLayout.addWidget(self.adtb)

        mkLayout.addWidget(QLabel("Stok Miktarı"))
        mkLayout.addWidget(self.miktartb)

        trLayout.addWidget(QLabel("Stok Türü"))
        trLayout.addWidget(self.turtb)

        kayitlarLayout.addLayout(adLayout)
        layout.addWidget(self.tableWidget) # Tabloyu layout'a ekle
        kayitlarLayout.addLayout(mkLayout)
        kayitlarLayout.addLayout(trLayout)
        kayitlarLayout.addLayout(butonlarLayout)

        layout.addLayout(kayitlarLayout)
        self.setLayout(layout)
   
       

    def secili_id_al(self):
        secili_satir = self.tableWidget.currentRow()  # Seçili satır indexi

        if secili_satir < 0:
            return None  # Hiçbir şey seçili değilse

        id_item = self.tableWidget.item(secili_satir, 0)  # 0. sütun ID
        if id_item:
            return id_item.text()

        return None

    def satir_tiklandi(self):
        self.secilenID = self.secili_id_al()
        print(self.secilenID)
        baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
        secilen1 = baglanti.cursor()
        secilen1.execute(f"SELECT * FROM ticarivt.stoklar WHERE id = '{self.secilenID}'")
        seciliKayit = secilen1.fetchone()
        print(seciliKayit, self.secilenID)
        baglanti.close()
       
        self.adtb.setText(seciliKayit[1])
        self.miktartb.setText(str(seciliKayit[2]))
        self.turtb.setText(seciliKayit[3])

    def kayitEkle(self):
        baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
        secilen1 = baglanti.cursor()
        yeniad = self.adtb.text()
        yenimiktar = self.miktartb.text()
        yenitur = self.turtb.text()
        # secilen1.execute("UPDATE ticarivt.stoklar SET stokadi = %s, stokmiktari = %s, tur=%s WHERE id= %s",(yeniad,yenimiktar,yenitur,self.secilenID))
        komut = "INSERT INTO ticarivt.stoklar (stokadi, stokmiktari, tur) VALUES (%s, %s, %s)"
        veri = (yeniad, yenimiktar, yenitur)
        secilen1.execute(komut, veri)

        baglanti.commit() # commit olmadan ekleme, silme ve değişikli veri tabanına işlenmez.
        baglanti.close()
        stoklar = stoklari_al()
        self.populate_table(stoklar)

    def kayitDuzenleme(self):
        baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
        secilen1 = baglanti.cursor()

        yeniad = self.adtb.text()
        yenimiktar = self.miktartb.text()
        yenitur = self.turtb.text()
        secilen1.execute("UPDATE ticarivt.stoklar SET stokadi = %s, stokmiktari = %s, tur=%s WHERE id= %s",(yeniad,yenimiktar,yenitur,self.secilenID))
        baglanti.commit() # commit olmadan ekleme, silme ve değişikli veri tabanına işlenmez.
        baglanti.close()
        stoklar = stoklari_al()
        self.populate_table(stoklar)

    def kayitSilme(self):
        baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
        secilen1 = baglanti.cursor()
        secilen1.execute(f"DELETE FROM ticarivt.stoklar WHERE id = '{self.secilenID}'")
        baglanti.commit()
        baglanti.close()
        stoklar = stoklari_al()
        self.populate_table(stoklar)
             

    def populate_table(self, stoklar):
        """Öğrenci listesini tabloya ekler"""
        self.tableWidget.setRowCount(len(stoklar))  # Satır sayısını belirle

        for row, student in enumerate(stoklar):
            for col, data in enumerate(student):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(data)))

# PyQt6 uygulamasını başlat
def main():
  app = QApplication(sys.argv)
  window = StokTablosu()
  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
    main()

