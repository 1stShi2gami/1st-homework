import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QCheckBox, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
# noinspection PyUnresolvedReferences
from registration import NewUserDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройка графического интерфейса приложения."""
        self.setMaximumSize(360, 220)
        self.setWindowTitle("3.1 – Login GUI")

        self.setUpMainWindow()
        self.show()  # показать окно

    def setUpMainWindow(self):
        """Настройка основных элементов главного окна."""
        self.login_is_successful = False

        # Создание заголовка
        login_label = QLabel("Login", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(160, 10)

        # Создание виджетов для имени пользователя и пароля
        username_label = QLabel("Никнейм", self)
        username_label.move(20, 54)

        self.username_edit = QLineEdit(self)
        self.username_edit.resize(254, 24)
        self.username_edit.move(90, 50)

        password_label = QLabel("Пароль", self)
        password_label.move(20, 86)

        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.resize(250, 24)
        self.password_edit.move(90, 82)

        # Создание QCheckBox для отображения пароля
        self.show_password_cb = QCheckBox("Показать пароль", self)
        self.show_password_cb.move(90, 110)
        self.show_password_cb.toggled.connect(self.displayPasswordIfChecked)

        # Создание кнопки для входа
        login_button = QPushButton("Войти", self)
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.clickLoginButton)

        # Создание Qlabel и QpushButton для регистрации
        not_member_label = QLabel("Еще не зарегистрированы?", self)
        not_member_label.move(120, 180)

        sign_up_button = QPushButton("Регистрация", self)
        sign_up_button.move(120, 200)
        sign_up_button.clicked.connect(self.createNewUser)

    def clickLoginButton(self):
        """
        Проверка совпадения имени пользователя и пароля с записями в файле users.txt.
        Если найдены, показывает QMessageBox и закрывает программу.
        Если нет, показывает предупреждение QMessageBox.
        """
        users = {}  # Словарь для хранения информации о пользователях
        file = "files/users.txt"

        try:
            with open(file, "r") as f:
                for line in f:
                    user_info = line.split(" ")
                    username_info = user_info[0]
                    password_info = user_info[1].strip("\n")
                    users[username_info] = password_info

            # Сбор информации о пользователе и пароле
            username = self.username_edit.text()
            password = self.password_edit.text()

            # Проверка совпадения имени пользователя и пароля с записями в словаре
            if username in users and users[username] == password:
                QMessageBox.information(self, "Успешный вход", "Вход выполнен успешно!")
                self.login_is_successful = True
                self.close()
            else:
                QMessageBox.warning(self, "Ошибка", "Неправильный логин или пароль")
        except FileNotFoundError:
            QMessageBox.warning(self, "Ошибка", "Файл пользователей не найден")

    def displayPasswordIfChecked(self, checked):
        """Отображение или скрытие пароля в зависимости от состояния чекбокса."""
        if checked:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def createNewUser(self):
        """Открытие диалогового окна для создания нового пользователя."""
        new_user_dialog = NewUserDialog()
        new_user_dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())