from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevirilecek: "))
        self.yazi = QLineEdit()
        icerik.addWidget(self.yazi)

        dügme = QPushButton("Çevir")
        icerik.addWidget(dügme)
        dügme.clicked.connect(self.xx)

        self.sonucl = QLabel("Sonuç: ")

        # icerik.addWidget(QLabel("Sonuç: "))
        icerik.addWidget(self.sonucl)
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def xx (self):
            aa = self.yazi.text()
            
            yazilacak = "Sonuç: " + str(int(aa)*2)
            self.sonucl.setText(yazilacak)

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()

uygulama.exec()