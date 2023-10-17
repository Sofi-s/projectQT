
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QSlider
from PIL import Image


class AlphaManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(10, 10, 555, 555)
        self.setWindowTitle('Изменение прозрачности')
        self.pixmap = QPixmap('orig.jpg')
        self.save = 'new.png'
        self.alpha = QSlider(Qt.Vertical, self)
        self.alpha.resize(33, 333)
        self.alpha.move(33, 33)
        self.alpha.setMinimum(0)
        self.alpha.setMaximum(255)
        self.alpha.valueChanged[int].connect(self.prozrachnost)

        self.alpha = QPixmap(self.pixmap)
        self.gogl = QLabel(self)
        self.gogl.resize(330, 330)
        self.gogl.move(100, 65)
        self.gogl.setPixmap(self.alpha)

    def prozrachnost(self, value):
        img = Image.open(self.fname)
        img = img.convert('RGBA')
        img.putalpha(value)
        self.alpha = QPixmap(self.save)
        self.image.setPixmap(self.alpha)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.exit(app.exec())


