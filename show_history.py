import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QLabel, QLineEdit, QListWidget


class History_window(QWidget):
    def __init__(self, data):
        super().__init__()
        self.initUI(data)

    def initUI(self, data):
        self.setGeometry(200, 100, 1500, 800)
        self.setWindowTitle('История перевода')

        self.button_back = QPushButton(self)
        self.button_back.resize(50, 50)
        self.button_back.move(10, 10)
        self.button_back.setText('Назад')
        self.button_back.clicked.connect(self.close)

        self.label = QLabel(self)
        self.label.resize(100, 25)
        self.label.move(10, 70)
        self.label.setText('История:')

        self.list_history = QListWidget(self)
        self.list_history.resize(1480, 690)
        self.list_history.move(10, 100)
        self.list_history.addItems(data)

