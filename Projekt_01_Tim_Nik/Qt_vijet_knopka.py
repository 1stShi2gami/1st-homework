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
        """Создание и расположение виджетов в главном окне."""
        self.times_pressed = 0  # Счетчик нажатий кнопки
        self.name_lable = QLabel("Don't push button.", self)  # Создание виджета
        self.name_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Выравнивание
        self.name_lable.move(60, 30)  # Перемещение
        self.button = QPushButton("Push ME!", self)  # Создание кнопки
        self.button.move(80, 70)  # Перемещение
        self.button.clicked.connect(self.buttonClicked)  # Обработка нажатия

    def buttonClicked(self):
        """Обработка нажатия на кнопку. Демонстрирует, как изменить текст для виджетов,
        обновлять их размеры и расположение, а также как закрывать окно в результате
        событий."""
        self.times_pressed += 1  # Счетчик нажатий кнопки
        if self.times_pressed == 1:  # Если счетчик равен 1
            self.name_lable.setText('Why u click me?')  # Текст для
        if self.times_pressed == 2:  # Если счетчик равен 2
            self.name_lable.setText('I warning you!?')  # #Текст для
            self.button.setText('Feeling Lucky!')  # Текст для кнопки
            self.button.adjustSize()  # Изменение размера к
            self.button.move(70, 70)  # Перемещение к
        if self.times_pressed == 3:
            print("Window closed")
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


# страница 48.