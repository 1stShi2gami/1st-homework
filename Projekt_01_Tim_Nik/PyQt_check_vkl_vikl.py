import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QCheckBox, QLabel)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("Пример CheckBox")
        self.UpMainWindow()
        self.show()

    def UpMainWindow(self):
        """ Создаём и располагаем виджеты в главном окне"""
        header_label = QLabel('В какие смены вы можете работать.', self)
        header_label.move(20, 10)
        header_label.setWordWrap(True)

        #устанавливаем флаги
        morning_cb = QCheckBox('Утро [8:00 - 12:00]', self)
        morning_cb.move(40, 60)
        morning_cb.toggle()
        morning_cb.toggled.connect(self.printSelected)

        after_cb = QCheckBox('День [13:00 - 20:00]', self)
        after_cb.move(40, 80)
        after_cb.toggled.connect(self.printSelected)

        night_cb = QCheckBox('Ночь [19:00 - 03:00]', self)
        night_cb.move(40, 100)
        night_cb.toggled.connect(self.printSelected)

        all_fucking_life_cb = QCheckBox('ВСЁ ГРЁБАННОЕ ВРЕМЯ', self)
        all_fucking_life_cb.move(40, 120)
        all_fucking_life_cb.toggled.connect(self.printSelected)

    def printSelected(self, checked):
        # печать текста объекта QCheckBox, когда он выбран или отменен. Используйте sender()
        # что бы определить, какой виджет посылает сигнал
        sender = self.sender()
        if checked:
            print(f'{sender.text()} выбран')
        else:
            print(f'{sender.text()} не выбран')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())