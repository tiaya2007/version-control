import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QFormLayout
)

class LoginForm(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Login")
        self.resize(300, 150)

        layout = QFormLayout()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        layout.addRow("Username:", self.username)
        layout.addRow("Password:", self.password)
        layout.addRow(self.login_button)
        self.setLayout(layout)

    def login(self):
        user = self.username.text()
        pwd = self.password.text()
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
        result = cur.fetchone()
        conn.close()
        if result:
            self.hide()
            self.order_form = OrderForm()
            self.order_form.show()
        else:
            QMessageBox.warning(self, "Error", "Username atau Password salah!")

class OrderForm(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Form Pemesanan Barang")
        self.resize(400, 200)

        layout = QFormLayout()
        self.nama = QLineEdit()
        self.barang = QLineEdit()
        self.jumlah = QLineEdit()
        self.alamat = QLineEdit()
        self.submit_button = QPushButton("Pesan")
        self.submit_button.clicked.connect(self.simpan_pesanan)

        layout.addRow("Nama Pemesan:", self.nama)
        layout.addRow("Nama Barang:", self.barang)
        layout.addRow("Jumlah:", self.jumlah)
        layout.addRow("Alamat:",