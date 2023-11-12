import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QSlider, QVBoxLayout, QWidget, QFileDialog, QLabel, \
    QTableWidgetItem
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb, QTransform, QMouseEvent
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageEnhance
import sqlite3
import csv


class his(QWidget):
    try:
        def __init__(self, *args):
            super().__init__()
            self.initUI()
            self.con = sqlite3.connect("db.sqlite")
            self.pushButton_alf.clicked.connect(self.rotate)


        def initUI(self):
            self.setWindowTitle('Вторая форма')
            uic.loadUi('form2.ui', self)
        def history_bd(self):
            try:
                timee = '13'
                a = 'doig'
                self.cursor = self.con.cursor()
                self.new_operation = (f'''INSERT
                INTO
                history(time, operation)
                VALUES({timee}, {a})''')
                try:
                    result = self.cur.execute(self.new_operation).fetchall()
                    self.tableWidget_2.setRowCount(len(result))
                    self.tableWidget_2.setColumnCount(len(result[0]))
                    for i, elem in enumerate(result):
                        for j, val in enumerate(elem):
                            self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))
                    self.cursor.commit()
                    self.cursor.close()
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
#
#
#     def alf(self):
#         self.cursor = self.con.cursor()
# SELECT * FROM your_table ORDER BY operation ASC

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = his()
    window.show()
    sys.exit(app.exec_())
