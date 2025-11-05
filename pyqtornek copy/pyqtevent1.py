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

        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def xx (self):
            aa = self.yazi.text()
            print(aa)

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()

uygulama.exec()