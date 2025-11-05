import mysql.connector
try:
  veritabani1 = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="1234", 
    database="ots" 
  )
  secilen1 = veritabani1.cursor()
  kayitlar = secilen1.execute("SELECT * FROM okul.rehber")
  kayitlar = secilen1.fetchall() 
  print(kayitlar)
  print("işlem tamam.")


except Exception as hata:
  print("Bir hata oluştu.")
  print(hata)

import sys
from PyQt6.QtWidgets import *


class TicariWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Inch çevirici")
        self.arayuz()


    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()


        label_cmdeger = QLabel("Cm değeri girin:"+ kayitlar[1][2])
        self.cmdeger_input = QLineEdit()
        layout.addWidget(label_cmdeger)
        layout.addWidget(self.cmdeger_input)


        cevir_button = QPushButton("Çevir")
        cevir_button.clicked.connect(self.mesaj)
        layout.addWidget(cevir_button)


        label_inch = QLabel("Inch değeri:")
        self.inch_input = QLineEdit()
        layout.addWidget(label_inch)
        layout.addWidget(self.inch_input)


        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
       
def main():
    app = QApplication(sys.argv)
    window = TicariWindow()
    QMessageBox.information(window, "Cm-Inch Çevirici", "Inch çevirici uygulamasına hoş geldiniz.")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
