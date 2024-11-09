import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):  # dlya pustogo okna
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):  # nastroika prilojeniya
        self.setGeometry(200, 100, 250, 250)
        self.setWindowTitle('Привер QLabel !')

        self.setUpMainWindow()
        self.show()  # otobrajenie okna (po umolchaniy skrito)

    def setUpMainWindow(self):
        hello_lable = QLabel(self)
        hello_lable.setText('Привет, мир!')
        hello_lable.move(50, 50)
        image = 'images/light.png'  # otobrajenie
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(50, 100)
        except FileNotFoundError as error:
            print(f'Файл не найден.\nError: {error}')


# zapusk progi
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
