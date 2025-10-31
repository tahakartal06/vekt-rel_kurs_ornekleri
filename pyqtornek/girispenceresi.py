# girispenceresi.py
import sys
from PyQt5 import QtWidgets, uic

# Buraya kendi .ui dosyanızın adını yazın
UI_FILE = "pyqtornek/untitled.ui"

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(UI_FILE, self)  # UI dosyasını yükle

        # Arayüzdeki widget'lara erişim (UI dosyasındaki objectName'ler ile)
        self.pushButton.clicked.connect(self.temizle)
        self.pushButton_2.clicked.connect(self.giris)

    def temizle(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def giris(self):
        kullanici = self.lineEdit.text()
        sifre = self.lineEdit_2.text()
        if kullanici == "admin" and sifre == "1234":
            QtWidgets.QMessageBox.information(self, "Başarılı", "Giriş başarılı!")
        else:
            QtWidgets.QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
