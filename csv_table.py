import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QSlider, QVBoxLayout, QWidget, QFileDialog, QLabel, \
    QTableWidgetItem
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb, QTransform
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw
import sqlite3
import csv


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()
        self.con = sqlite3.connect("db.sqlite")
        self.filter_bd()
        self.loadTable('images2.csv')

    def initUI(self):
        self.setWindowTitle('Вторая форма')
        uic.loadUi('form2.ui', self)

    def filter_bd(self):
        self.cur = self.con.cursor()
        tab1 = "SELECT * FROM filters"
        try:
            result = self.cur.execute(tab1).fetchall()
            self.tabWid_bd.setRowCount(len(result))
            self.tabWid_bd.setColumnCount(len(result[0]))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tabWid_bd.setItem(i, j, QTableWidgetItem(str(val)))
        except Exception as e:
            print(e)

    def loadTable(self, table_name):
        try:
            with open(table_name) as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                title = next(reader)
                self.tableWidget_csv.setColumnCount(len(title))
                self.tableWidget_csv.setHorizontalHeaderLabels(title)
                self.tableWidget_csv.setRowCount(0)
                for i, row in enumerate(reader):
                    self.tableWidget_csv.setRowCount(
                        self.tableWidget_csv.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.tableWidget_csv.setItem(i, j, QTableWidgetItem(str(elem)))
            self.tableWidget_csv.resizeColumnsToContents()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SecondForm()
    window.show()
    sys.exit(app.exec_())
