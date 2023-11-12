from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QPixmap
from PIL import Image

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример")
        self.setGeometry(100, 100, 800, 600)
        self.show()
        self.keyPressEvent = self.mousePressEvent()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_R:
            print(f"Обрезка: x={self.x}, y={self.y}, x1={self.x1}, y1={self.y1}")
            try:
                print('oi')
                with Image.open(self.new_file_name) as im:
                    cropped_img = im.crop((self.x, self.y, self.x1, self.y1))
                    cropped_img.save(self.new_file_name)
                    self.pixmap = QPixmap(self.new_file_name)
                    self.izobr.setPixmap(self.pixmap)


            except Exception as e:
                print(e)

    def mousePressEvent(self, event: QMouseEvent):
        print(event.button())
        try:
            if event.button() == Qt.LeftButton:
                self.x = event.x()
                self.y = event.y()
            if event.button() == Qt.RightButton:
                self.x1 = event.x()
                self.y1 = event.y()
            print(f"Координаты нажатия: x={self.x}, y={self.y}, x1={self.x1}, y1={self.y1}")
        except Exception as e:
            print(e)

# Создаем приложение Qt
app = QApplication([])

# Создаем экземпляр виджета
widget = MyWidget()

# Запускаем главный цикл приложения
app.exec()
