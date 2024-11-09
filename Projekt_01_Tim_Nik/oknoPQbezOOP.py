import sys
from PyQt6.QtWidgets import QWidget, QApplication
from guiqwt.pyplot import title

app = QApplication(sys.argv)
window = QWidget()
window.show()
sys.exit(app.exec())