from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı Adı: "))
        self.ka = QLineEdit()
        icerik.addWidget(self.ka)

        deneme = QVBoxLayout()
        deneme.addWidget(QLabel("Kullanıcı Şifresi: "))
        self.sf = QLineEdit()
        self.sf.setEchoMode(QLineEdit.EchoMode.Password)
        icerik.addWidget(self.sf)

        icerik.addLayout(deneme)

        dügme = QPushButton("Giriş Yap")
        icerik.addWidget(dügme)
        dügme.clicked.connect(self.xx)

        self.sonucl = QLabel("Sonuç: ")

        # icerik.addWidget(QLabel("Sonuç: "))
        icerik.addWidget(self.sonucl)
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def xx (self):
            aa = self.ka.text()
            bb = self.sf.text()
            if aa == "adm" and bb == "123":
                 yazilacak = "Sonuç: " + "Giriş Başarılı"
            else:
                 yazilacak = "Sonuç: " + "Yetki yok"
               
            
            self.sonucl.setText(yazilacak)

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()

uygulama.exec()