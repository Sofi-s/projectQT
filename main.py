import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QSlider, QVBoxLayout, QWidget, QFileDialog, QLabel, \
    QTableWidgetItem,QCommandLinkButton
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb, QTransform, QMouseEvent
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageEnhance
import sqlite3
import csv
import datetime


class ImageProcessor(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi('photoshop2.ui', self)
        self.image = None
        self.image_path = None
        self.new_file_name = "new.png"
        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0]
        if not self.filename:
            exit()
        img = Image.open(self.filename)
        img.save(self.new_file_name)
        self.pixmap = QPixmap(self.filename).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
        self.izobr.setPixmap(self.pixmap)
        self.pravos.clicked.connect(self.rotate)
        self.levod.clicked.connect(self.rotate)
        self.pravod.clicked.connect(self.rotate)
        self.izobr.setPixmap(self.pixmap)
        self.izobr.setStyleSheet("background-color: white;")
        self.izobr.mousePressEvent = self.mousePressEvent1
        self.angle = 0
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setValue(255)
        # self.horizontalSlider_4.setMinimum(0)
        # self.horizontalSlider_4.setMaximum(100)
        # self.horizontalSlider_4.setValue(0)
        # self.con = sqlite3.connect("db.sqlite")
        # self.bd()
        self.push_bd.clicked.connect(self.open_second_form)
        # self.slider.valueChanged.connect(self.visibility)
        # for button in self.channelButtons.buttons():
        self.comBY_yvel.clicked.connect(lambda: self.yark_yvelich_1)

        self.yarkost.clicked.connect(self. adjustBrightness)
        # #  self.horizontalSlider.valueChanged.connect(self.adjustBrightness)
        #   self.razmutie.clicked.connect(self.blurImage)
        self.pushBu_orig.clicked.connect(self.orig_im)
        tec_tame = 0
        difference = ''
        #self.prozrachnost.clicked.connect(self.prozrachnost)
        self.horizontalSlider_3.valueChanged[int].connect(self.adjustTransparency)
        self.sepeia.clicked.connect(self.applySepia)
        self.blue.clicked.connect(self.applyBlueEffect)
        self.green.clicked.connect(self.applyGreenEffect)
        self.hb.clicked.connect(self.white_black)
        self.negative.clicked.connect(self.Negative)
        self.pushButton_red.clicked.connect(self.applyRedEffect)
        self.hb.clicked.connect(self.white_black)
        self.pravos.clicked.connect(self.rotate)
        self.pravod.clicked.connect(self.rotate)
        self.levod.clicked.connect(self.rotate)
        # self.mouse()
        self.pushButton_9.clicked.connect(self.saveImage)
        self.con = sqlite3.connect("db.sqlite")
        self.query = """DELETE from history"""
        print(self.query)
        self.cursor = self.con.cursor()
        self.cursor.execute(self.query)
        self.con.commit()
        self.x = self.y = self.x1 = self.y1 = 0


    def loadImage(self, path):
        self.image = Image.open(path).resize(430, 430)

    def displayImage(self, processed_image=None):
        print(0)
        if processed_image is not None:
            self.image = processed_image

        if self.image is not None:
            print("d")
            qImg = QImage(self.image.tobytes("raw", "RGBA"), self.image.width, self.image.height,
                          QImage.Format_RGBA8888)
            pixmap = QPixmap.fromImage(qImg).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
            self.izobr.setPixmap(pixmap)

    def adjustBrightness(self):
        try:
            with Image.open(self.new_file_name) as im:
                self.enhancer = ImageEnhance.Contrast(im)
                self.factor = 2  # gives original image
                self.im_output = self.enhancer.enhance(self.factor)
                self.im_output.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)


    def adjustTransparency(self, value):
        try:
            transp = int(self.horizontalSlider_3.value())
            img = Image.open(self.new_file_name)
            img = img.convert('RGBA')
            img.putalpha(transp)
            img.save(self.new_file_name)
            self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
            self.izobr.setPixmap(self.pixmap)


        except Exception as e:
            print(e)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_R:
            print(f"Обрезка: x={self.x}, y={self.y}, x1={self.x1}, y1={self.y1}")
            try:
                with Image.open(self.new_file_name) as im:
                    cropped_img = im.crop(self.x, self.y, self.x1, self.y1)
                    cropped_img.save(self.new_file_name)
                    self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                    self.izobr.setPixmap(self.pixmap)
                    ImageProcessor.tec_tame = datetime.now()

            except Exception as e:
                print(e)

    # code
    def mousePressEvent1(self, event):
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

    # def obrezka(self):
    #     self.mouse()
    #     try:
    #         with Image.open(self.new_file_name) as im:
    #             cropped_img = im.crop(self.x.split(), (self.y)
    #             cropped_img.save(self.new_file_name)
    #             self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
    #             self.izobr.setPixmap(self.pixmap)
    #             ImageProcessor.tec_tame = datetime.now()
    #
    #     except Exception as e:
    #         print(e)


    def yark_yvelich(self, n):
        self.n = self.n + 0.5

    def yark_yvelich_1(self):
        try:
            with Image.open(self.new_file_name) as im:
                self.enhancer = ImageEnhance.Contrast(im)
                self.factor = 1.5
                self.comBY_yvel.clicked.connect(lambda: self.yark_yvelich(self.factor))
                self.im_output = self.enhancer.enhance(self.factor)
                self.im_output.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)


    def applySepia(self):
        try:
            with Image.open(self.new_file_name) as im:
                pix = im.load()
                draw = ImageDraw.Draw(im)
                width = im.size[0]
                height = im.size[1]
                for i in range(width):
                    for j in range(height):
                        a = pix[i, j][0]
                        b = pix[i, j][1]
                        c = pix[i, j][2]
                        S = (a + b + c) // 4
                        a = S + 75 * 2
                        b = S + 75
                        c = S
                        if (a > 255):
                            a = 255
                        if (b > 255):
                            b = 255
                        if (c > 255):
                            c = 255
                        draw.point((i, j), (a, b, c))
                im.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)

    def applySepias(self, value):
        try:
            transp = int(self.horizontalSlider_4.value())
            img = Image.open(self.new_file_name)
            # img = img.convert('RGBA')
            img.putalpha(transp)
            pix = img.load()
            draw = ImageDraw.Draw(img)
            width = img.size[0]
            height = img.size[1]
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    S = (a + b + c) // 3
                    a = S + transp * 2
                    b = S + transp
                    c = S
                    if (a > 255):
                        a = 255
                    if (b > 255):
                        b = 255
                    if (c > 255):
                        c = 255
                    draw.point((i, j), (a, b, c))
            img.save(self.new_file_name)
            self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
            self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)

    def white_black(self):
        try:
             with Image.open(self.new_file_name) as img:
                 gray_img = img.convert("L")
                 gray_img.save(self.new_file_name)
                 self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                 self.izobr.setPixmap(self.pixmap)
                 ImageProcessor.tec_tame = datetime.now()
        except Exception as e:
            print(e)

    def orig_im(self):
        try:
            with Image.open(self.filename) as im:

                self.im.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)


    def applyRedEffect(self):
        try:
            with Image.open(self.new_file_name) as img:
                red, green, blue = img.split()
                zeroed_band = red.point(lambda _: 0)
                self.red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
                self.red_merge.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)

    def applyBlueEffect(self):
        try:
            with Image.open(self.new_file_name) as img:
                red, green, blue = img.split()
                zeroed_band = red.point(lambda _: 0)
                self.blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))
                self.blue_merge.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()

        except Exception as e:
            print(e)

    def applyGreenEffect(self):
        try:
            with Image.open(self.new_file_name) as img:
                red, green, blue = img.split()
                zeroed_band = red.point(lambda _: 0)
                self.green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
                self.green_merge.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)



    def Negative(self):
        try:
            with Image.open(self.new_file_name) as im:
                pix = im.load()
                draw = ImageDraw.Draw(im)
                width = im.size[0]
                height = im.size[1]
                for i in range(width):
                    for j in range(height):
                        a = pix[i, j][0]
                        b = pix[i, j][1]
                        c = pix[i, j][2]
                        draw.point((i, j), (255 - a, 255 - b, 255 - c))
                im.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)

        except Exception as e:
            print(e)

    def saveImage(self):
        print(0)
        img = Image.open(self.new_file_name)
        img.save(QFileDialog.getSaveFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0])

    def rotate(self):
        with Image.open(self.new_file_name) as im:

            if self.sender() is self.pravod:
                self.image = im.rotate(90)

            if self.sender() is self.pravos:
                self.image = im.rotate(180)
            if self.sender() is self.levod:
                self.image = im.rotate(270)
            self.image.save(self.new_file_name)
            self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)

    def open_second_form(self):
        self.second_form = SecondForm(self, "Данные для второй формы")
        self.second_form.show()




class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()
        self.con = sqlite3.connect("db.sqlite")
        self.filter_bd()
        self.loadTable('images2.csv')
        self.history_bd()


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

    def history_bd(self):
        #print("h")
        try:
            self.cursor = self.con.cursor()
            self.query = f'''INSERT
                        INTO history(time, operation)
                        VALUES('{ImageProcessor.tec_tame}', '{"erger"}')'''
            self.new_operation = self.query
            self.cur.execute(self.query)
            print(self.query)
            try:
                result = self.cur.execute("Select * from history").fetchall()
                self.tableWidget_2.setRowCount(len(result))
                self.tableWidget_2.setColumnCount(len(result[0]))
                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))
            except Exception as e:
                print(e)
            self.con.commit()


        except Exception as e:
            print(e)


if __name__ == "__main__":
    print(datetime.datetime.now())
    app = QApplication(sys.argv)
    window = ImageProcessor()
    window.show()
    sys.exit(app.exec_())
