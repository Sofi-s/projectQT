# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtCore import QTimer
# from PyQt5.QtGui import QCursor
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.label = QLabel()
#         self.setCentralWidget(self.label)
#
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_cursor_position)
#         self.timer.start(100)  # Обновление каждые 100 мс
#
#     def update_cursor_position(self):
#         cursor_pos = QCursor.pos()
#         self.label.setText(f'Координаты курсора: x={cursor_pos.x()}, y={cursor_pos.y()}')
#
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('WheelEvent')
#
#         btn = QPushButton('Click me!', self)
#         btn.setGeometry(100, 80, 100, 30)
#         btn.clicked.connect(self.buttonClicked)
#
#         self.show()
#
#     def buttonClicked(self):
#         print('Button clicked!')
#
#     def wheelEvent(self, event):
#         numDegrees = event.angleDelta().y() / 8
#         numSteps = numDegrees / 15
#
#         print('numDegrees =', numDegrees, 'numSteps =', numSteps)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyWindow()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('MousePressEvent')
#
#         btn = QPushButton('Click me!', self)
#         btn.setGeometry(100, 80, 100, 30)
#         btn.clicked.connect(self.buttonClicked)
#
#         self.show()
#
#     def buttonClicked(self):
#         print('Button clicked!')
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             print('Left mouse button pressed')
#         elif event.button() == Qt.RightButton:
#             print('Right mouse button pressed')
#         elif event.button() == Qt.MidButton:
#             print('Middle mouse button pressed')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyWindow()
#     sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent

class MyWidget(QWidget):
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            x = event.x()
            y = event.y()
            print(f"Координаты нажатия: x={x}, y={y}")

# Создаем приложение Qt
app = QApplication([])

# Создаем экземпляр виджета
widget = MyWidget()

# Устанавливаем размер виджета
widget.resize(800, 600)

# Отображаем виджет
widget.show()

app.exec()