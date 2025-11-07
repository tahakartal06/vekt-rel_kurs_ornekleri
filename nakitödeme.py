import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class nakitödeme(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Nakit Ödeme ve Para Üstü Hesaplama")
        
        # Ana Layout
        layout = QVBoxLayout()

        # Ürün Fiyatı Etiketi ve Girişi
        self.product_label = QLabel("Ürün Fiyatı (TL):")
        self.product_input = QLineEdit()
        layout.addWidget(self.product_label)
        layout.addWidget(self.product_input)

        # Kullanıcı Ödeme Etiketi ve Girişi
        self.payment_label = QLabel("Ödenen Miktar (TL):")
        self.payment_input = QLineEdit()
        layout.addWidget(self.payment_label)
        layout.addWidget(self.payment_input)

        # Sonuç Etiketi
        self.result_label = QLabel("Para Üstü: ")
        layout.addWidget(self.result_label)

        # Hesaplama Düğmesi
        self.calculate_button = QPushButton("Para Üstünü Hesapla")
        self.calculate_button.clicked.connect(self.calculate_change)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)
        self.show()

    def calculate_change(self):
        try:
            # Kullanıcıdan alınan veriler
            product_price = float(self.product_input.text())  # Ürün fiyatı
            paid_amount = float(self.payment_input.text())    # Ödenen miktar

            # Para üstü hesaplama
            if paid_amount < product_price:
                self.result_label.setText("Ödenen miktar yetersiz!")
            else:
                change = paid_amount - product_price
                self.result_label.setText(f"Para Üstü: {change:.2f} TL")
        except ValueError:
            self.result_label.setText("Lütfen geçerli bir sayı girin.")


app = QApplication(sys.argv)
ex = nakitödeme()
sys.exit(app.exec_())