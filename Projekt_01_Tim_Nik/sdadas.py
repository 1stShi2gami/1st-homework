import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QCheckBox, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap

from registration import NewUserDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(360, 220)
        self.setWindowTitle("PyQt - Log In")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # Создайте и расположите виджеты в главном окне
        self.login_is_successful = False

        login_label = QLabel('Login', self)
        login_label.move(160, 10)
        login_label.setFont(QFont('Arial', 20))

        # Создайте виджеты для имени пользователя и пароля
        username_label = QLabel('Имя пользователя:', self)
        username_label.move(20, 54)

        self.username_edit = QLineEdit(self)
        self.username_edit.move(90, 50)
        self.username_edit.resize(250, 24)

        # Создайте виджеты для пароля
        password_label = QLabel('Пароль:', self)
        password_label.move(20, 90)

        self.password_edit = QLineEdit(self)
        self.password_edit.move(90, 86)
        self.password_edit.resize(250, 24)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        # Создаем QCheckBox для отображения пароля
        self.show_password_cb = QCheckBox('Показать пароль', self)
        self.show_password_cb.move(90, 110)
        self.show_password_cb.toggled.connect(self.displayPasswordIfChecked)

        # Создаем QPushButton для входа
        login_button = QPushButton('Войти', self)
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.clickLoginButton)

        # Создайте QLabel и QPushButton для регистрации
        not_member_label = QLabel('Вы не зарегистрированы', self)
        not_member_label.move(20, 186)

        sign_up_button = QPushButton('Зарегистрироваться', self)
        sign_up_button.move(120, 180)
        sign_up_button.clicked.connect(self.createNewUser)

    def clickLoginButton(self):
        # Проверьте, совпадают ли имя пользователя и пароль с любыми
        # существующими записями в файле users.txt.
        # Если они найдены, покажите QMessageBox и закройте программу.
        # Если нет, покажите предупреждение QMessageBox.

        user = {}  # создаем словарь для хранения информации о пользователях
        file = r"E:\python projekts uu\Shigami\Projekt_01_Tim_Nik\users.txt"

        try:
            with open(file, 'r') as f:
                for line in f:
                    user_info = line.split()  # Разделение по пробелам
                    username_info = user_info[0]
                    password_info = user_info[1].strip('\n')
                    user[username_info] = password_info

            username = self.username_edit.text()
            password = self.password_edit.text()

            if username in user and user[username] == password:
                QMessageBox.information(self, 'Вход', 'Добро пожаловать!', QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.login_is_successful = True
                self.close()  # Закройте окно входа в систему
                self.openApplicationWindow()
            else:
                QMessageBox.warning(self, 'Вход', 'Неверный логин или пароль', QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Ошибка", f"""<p>Файл не найден.</p>
                                <p>Ошибка: {error}</p>""",
                                QMessageBox.StandardButton.Ok)
            """Создайте файл, если его не существует"""
            f = open(file, 'w')

    def displayPasswordIfChecked(self, checked):
        # если QCheckButton включен, просмотрите пароль.
        # В противном случае скрыть пароль
        if checked:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def createNewUser(self):
        # Создайте нового пользователя
        self.create_new_user_window = NewUserDialog()
        self.create_new_user_window.show()

    def openApplicationWindow(self):
        # Открываем макет главного окна после входа
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self, event):
        """Реализуйте событие закрытия для отображения
         QMessageBox перед закрытием."""
        if self.login_is_successful:
            event.accept()
        else:
            answer = QMessageBox.question(
                self, 'Выйти из приложения?',
                'Вы уверены, что хотите выйти из приложения?',
                QMessageBox.StandardButton.No
                | QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.Yes)
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())