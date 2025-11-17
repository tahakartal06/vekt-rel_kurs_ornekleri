# stok.py
import sys
from PyQt6.QtWidgets import *

class StokkPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stok Modulu")

        central_widget = QWidget()
        layout = QVBoxLayout()

        buton1 = QPushButton("Stok Ekle")
        buton2 = QPushButton("Stok Listesi")
        buton3 = QPushButton("...")
        buton4 = QPushButton("...")
        buton5 = QPushButton("ÇIKIŞ")

       
        buton1.clicked.connect(self.stokEkle)
        buton2.clicked.connect(self.stokListele)
        buton5.clicked.connect(lambda: sys.exit())

        layout.addWidget(buton1)
        layout.addWidget(buton2)
        layout.addWidget(buton3)
        layout.addWidget(buton4)
        layout.addWidget(buton5)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def stokEkle(self):
        import stokekle
        self.ekleme_penceresi = stokekle.StokEkleme()
        # self.ekleme_penceresi.move(-500,200)
        self.ekleme_penceresi.show()
   
    def stokListele(self):
        import stokliste
        self.liste_penceresi = stokliste.StokTablosu()
        # self.liste_penceresi.move(-500,400)
        self.liste_penceresi.show()

    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
       
def main():
    app = QApplication(sys.argv)
    window = StokkPenceresi()
    # QMessageBox.information(window, "Cm-Inch Çevirici", "Inch çevirici uygulamasına hoş geldiniz.")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


