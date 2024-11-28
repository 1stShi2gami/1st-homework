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
        users = {}
        file = r"E:\python projekts uu\Shigami\Projekt_01_Tim_Nik\PyQt_GUI_log_pas.py/users.txt"

        # Проверяем наличие файла и создаем его, если он отсутствует
        if not os.path.exists(file):
            os.makedirs(os.path.dirname(file), exist_ok=True)
            with open(file, "w") as f:
                pass  # Создаем пустой файл

        try:
            with open(file, "r") as f:
                for line in f:
                    user_info = line.split('')
                    username_info = user_info[0]
                    password_info = user_info[1].strip("\n")
                    users[username_info] = password_info

            username = self.username_edit.text()
            password = self.password_edit.text()

            # Проверяем, есть ли пользователь в словаре и совпадает ли пароль
            if username in users and users[username] == password:
                QMessageBox.information(self,
                                        "Login Successful!",
                                        "Login Successful!",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.login_is_successful = True
                self.close()
                self.openApplicationWindow()
            else:
                QMessageBox.warning(self, "Сообщение об ошибке",
                                    "Имя пользователя или пароль неверны.",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)

        except Exception as error:
            QMessageBox.warning(self, "Ошибка",
                                f"""<p>Произошла ошибка при работе с файлом.</p> 
                                 <p>Ошибка: {error}</p>""",
                                QMessageBox.StandardButton.Ok)

    def displayPasswordIfChecked(self, checked):
        """Если QCheckButton включен, просмотрите пароль.
        В противном случае замаскируйте пароль, чтобы другие
        не могли его увидеть."""
        if checked:
            self.password_edit.setEchoMode(
                QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.password_edit.setEchoMode(
                QLineEdit.EchoMode.Password)

    def createNewUser(self):
        """Открыть диалог для создания новой учетной записи."""
        self.create_new_user_window = NewUserDialog()
        self.create_new_user_window.show()

    def openApplicationWindow(self):
        """Открыть главное окно приложения."""
        # Код для открытия главного окна приложения
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self, event):
        """Реализуйте событие закрытия для отображения
        QmessageBox перед закрытием."""
        if self.login_is_successful:
            event.accept()
        else:
           answer = QMessageBox.question(
                self, "Выйти из приложения?",
                "Вы уверены, что хотите выйти из приложения?",
                QMessageBox.StandardButton.No | \
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.Yes)
        if answer == QMessageBox.StandardButton.Yes:
            event.accept()
        if answer == QMessageBox.StandardButton.No:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
