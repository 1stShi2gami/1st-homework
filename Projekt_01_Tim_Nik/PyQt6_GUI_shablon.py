import sys

from PyQt6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Пустое окно в PyQt")
        self.show()

        # QTimer.singleShot(5000, self.close)  Закрыть окно через 5 секунд

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())