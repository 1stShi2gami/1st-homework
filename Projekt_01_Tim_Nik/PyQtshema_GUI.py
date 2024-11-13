import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("2.1 - User Profile GUI")
        self.setUpMainWindow()
        self.show()

    def createimageLable(self):
        """Открывает файлы изображений и создаёт метки изображений."""
        images = ['images/shapka.png',
                  'images/profile.png']
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == 'images/profile.png':
                        label.move(80, 20)
            except FileNotFoundError as error:
                print(f'Ошибка.\nError: {error}')

    def setUpMainWindow(self):
        self.createimageLable()
        user_label = QLabel(self)
        user_label.setText('Tim Tim')
        user_label.setFont(QFont('Bookman Old Style', 20))
        user_label.move(85, 140)
        bio_label = QLabel(self)
        bio_label.setText('Biographies')
        bio_label.setFont(QFont('Bookman Old Style', 17))
        bio_label.move(15, 170)
        about_label = QLabel(self)
        about_label.setText('im a low skill programmer')
        about_label.setWordWrap(True)
        about_label.move(15, 190)
        skills_label = QLabel(self)
        skills_label.setText("Умения")
        skills_label.setFont(QFont("Bookman Old Style", 17))
        skills_label.move(15, 240)
        languages_label = QLabel(self)
        languages_label.setText("Python | PHP | SQL | JavaScript")
        languages_label.move(15, 260)
        experience_label = QLabel(self)
        experience_label.setText("Опыт")
        experience_label.setFont(QFont("Bookman Old Style", 17))
        experience_label.move(15, 290)
        developer_label = QLabel(self)
        developer_label.setText("Python Разработчик")
        developer_label.move(15, 310)
        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Март 2011 - настоящее время")
        dev_dates_label.setFont(QFont("Bookman old style", 10))
        dev_dates_label.move(15, 330)
        driver_label = QLabel(self)
        driver_label.setText("Водитель доставки пиццы")
        driver_label.move(15, 350)
        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Aug 2015 - Dec 2017")
        driver_dates_label.setFont(QFont("Bookman old style", 10))
        driver_dates_label.move(15, 370)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())