import sys


from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
from PyQt6.QtCore import Qt



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройка графического интерфейса окна"""
        self.setMaximumSize(310, 130)
        self.setWindowTitle("QlineEdit 1st")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создание и расположение виджетов в главном окне"""

        QLabel('Введите Логин.', self).move(70, 10) # логин
        name_lable = QLabel('Логин.', self)
        name_lable.move(20,50) # логин перемещение

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(210, 20)
        self.name_edit.move(70, 50)

        clear_button = QPushButton('Clear', self)
        clear_button.move(140, 90)
        clear_button.clicked.connect(self.clearText)

        accept_button = QPushButton('Accept', self)
        accept_button.move(200, 90)
        accept_button.clicked.connect(self.acceptText)

    def clearText(self):
        """Очистка поля ввода"""
        self.name_edit.clear()

    def acceptText(self):
        """Принять ввод пользователя в виджет QLineEdit"""
        print(self.name_edit.text())
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()) 