import mysql.connector
try:
  veritabani1 = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="ticarivt" # ots = okultakipsistemi
  )
  secilen1 = veritabani1.cursor()
  # secilen1.execute("UPDATE kullanicilar SET numara = '05364445566' WHERE ad= 'Arda Güler'")
  kayitlar = secilen1.execute("SELECT * FROM ticarivt.kullanicilar")
  kayitlar = secilen1.fetchall() # commit olmadan ekleme, silme ve değişikli veri tabanına işlenmez.
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
        self.setWindowTitle("Ödeme Kısmı")
        

        pencere_ici = QWidget()
        layout = QVBoxLayout()

        buton1 = QPushButton("NAKİT")
        buton2 = QPushButton("HAVALE")
        buton3 = QPushButton("KREDİKARTI")
        buton4 = QPushButton("HEDİYE ÇEKİ")
        buton5 = QPushButton("ÇIKIŞ")

        buton1.clicked.connect(self.nakitödeme)
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

    def nakitödeme(self):
        import nakitödeme
        nk = nakitödeme.nakitödeme()
        self.nk.move(-400,200)
        self.nk.show()
         
        


    def kapa(self):
        sys.exit()


    def stok(self):
        import stok
        self.sp = stok.StokkPenceresi()
        self.sp.move(-600,200)
        self.sp.show()
        # self.close()



    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
       
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("iŞLETME V1")
        self.arayuz()


    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()


        # label_username = QLabel("Kullanıcı Adı:")
        label_username = QLabel("Kullanıcı Adı:")
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


        # Kullanıcı adı ve şifreyi kontrol etme - Örnek amaçlı basit bir kontrol
        secilen1.execute(f"SELECT * FROM ticarivt.kullanicilar where ka  = '{username}'")
        kullanici = secilen1.fetchall()
        if username == kullanici[0][1] and password == kullanici[0][2]:
            # self.close()  # Login penceresini kapat
            # import ticari
            # self.xx = ticari.TicariWindow()
            self.xx = TicariWindow()
            self.xx.show()
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")


    def open_ticari_window(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nÖdeme kısmındasınız.")
       





def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()