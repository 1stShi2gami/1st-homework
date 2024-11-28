import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel)
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 100)
        self.setWindowTitle("PyQt - knopka experement")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()) # QTimer.singleShot(5000, self.close)  Закрыть окно через 5 секунд