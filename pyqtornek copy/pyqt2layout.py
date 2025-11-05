from PyQt6.QtWidgets import*

uygulama = QApplication([])

icerik = QHBoxLayout()

# icerik = QVBoxLayout() dikey yapar

icerik.addWidget(QLabel("Çevirilecek: "))
icerik.addWidget(QLineEdit())
icerik.addWidget(QPushButton("Çevir")) 
icerik.addWidget(QLabel("Sonuç: "))

icerik1 = QVBoxLayout()

icerik1.addWidget(QLabel("Çevirilecek1: "))
icerik1.addWidget(QLineEdit())
icerik1.addWidget(QPushButton("Çevir1"))
icerik1.addWidget(QLabel("Sonuç: "))

buyukicerik = QVBoxLayout()
buyukicerik.addLayout(icerik)
buyukicerik.addLayout(icerik1)

pencere = QMainWindow()
pencere.setWindowTitle("Çeviri")

araclar = QWidget()
araclar.setLayout(buyukicerik)
pencere.setCentralWidget(araclar)
pencere.show()

uygulama.exec()