import mysql.connector
try:
  veritabani1 = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="1234", 
    database="ots" 
  )
  secilen1 = veritabani1.cursor()
  kayitlar = secilen1.execute("SELECT * FROM rehber")
  kayitlar = secilen1.fetchall() 
  print(kayitlar)
  print("işlem tamam.")


except Exception as hata:
  print("Bir hata oluştu.")
  print(hata)


# proje3.py
import sys
from PyQt6.QtWidgets import *


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Login Ekranı")
        self.arayuz()


    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()


        # label_username = QLabel("Kullanıcı Adı:")
        label_username = QLabel("Kullanıcı Adı:"+kayitlar[1][2])
        self.username_input = QLineEdit()
        layout.addWidget(label_username)
        layout.addWidget(self.username_input)


        label_password = QLabel("Şifre:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(label_password)
        layout.addWidget(self.password_input)


        login_button = QPushButton("Giriş Yap")
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)


        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()


        
        if username == "1" and password == "1":
            self.xx = TicariWindow()
            self.xx.show()
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")


    def open_ticari_window(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
       


class TicariWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Inch çevirici")




        pencere_ici = QWidget()
        layout = QVBoxLayout()


        buton1 = QPushButton("STOK")
        buton2 = QPushButton("CARİ")
        buton3 = QPushButton("DEPO")
        buton4 = QPushButton("MUHASEBE")
        buton5 = QPushButton("ÇIKIŞ")


        buton1.clicked.connect(self.stok)
        buton4.clicked.connect(self.mesajgoster)
       
        buton5.clicked.connect(lambda: sys.exit())


        layout.addWidget(buton1)
        layout.addWidget(buton2)
        layout.addWidget(buton3)
        layout.addWidget(buton4)
        layout.addWidget(buton5)


        pencere_ici.setLayout(layout)
        self.setCentralWidget(pencere_ici)


    def mesajgoster(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Bilgilendirme!")
        dlg.setText("Buradaki bilgiyi öğrendin.")
        dlg.exec()


    def kapa(self):
        sys.exit()


    def stok(self):
        import stok
        self.sp = stok.StokkPenceresi()
        self.sp.move(-600,200)
        self.sp.show()
        


    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
       


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
