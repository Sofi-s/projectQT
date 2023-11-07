import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QSlider, QVBoxLayout, QWidget, QFileDialog, QLabel, \
    QTableWidgetItem
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb, QTransform
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw
import sqlite3
from datetime import datetime


class ImageProcessor(QDialog):

    tec_tame = 0
    difference = ''

    def __init__(self):
        super().__init__()
        uic.loadUi('photoshop2.ui', self)
        self.image = None
        self.image_path = None
        self.new_file_name = "new.png"
        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0]
        img = Image.open(self.filename)
        img.save(self.new_file_name)
        self.pixmap = QPixmap(self.filename).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
        self.izobr.setPixmap(self.pixmap)
        # self.displayImage()
        self.pravos.clicked.connect(self.rotate)
        self.levod.clicked.connect(self.rotate)
        self.pravod.clicked.connect(self.rotate)
        self.izobr.setPixmap(self.pixmap)
        self.izobr.setStyleSheet("background-color: white;")
        self.angle = 0
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setValue(255)
        self.horizontalSlider_4.setMinimum(0)
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setValue(0)
        # self.con = sqlite3.connect("db.sqlite")
        # self.bd()
        self.push_bd.clicked.connect(self.open_second_form)
        # self.slider.valueChanged.connect(self.visibility)
        # for button in self.channelButtons.buttons():

        #   self.yarkost.clicked.connect(self.adjustBrightness)
        # #  self.horizontalSlider.valueChanged.connect(self.adjustBrightness)
        #   self.razmutie.clicked.connect(self.blurImage)
        #   self.horizontalSlider_2.valueChanged.connect(self.blurImage)
        #
        #   # self.prozrachnost.clicked.connect(self.prozrachnost)
        self.horizontalSlider_3.valueChanged[int].connect(self.adjustTransparency)
        #   self.alpha = self.findChild(QSlider, 'horizontalSlider_3')
        #   self.alpha.valueChanged[int].connect(self.adjustTransparency)
        #
        self.sepeia.clicked.connect(self.applySepia)
        self.horizontalSlider_4.valueChanged.connect(self.applySepias)
        #

        self.blue.clicked.connect(self.channel)
        self.hb.clicked.connect(self.channel)
        self.yellow.clicked.connect(self.channel)
        #   self.horizontalSlider_5.valueChanged.connect(self.applyCyanotype)
        #
        #   self.negative.clicked.connect(self.applyNegative)
        #   self.horizontalSlider_6.valueChanged.connect(self.applyNegative)
        #
        #   self.yellow.clicked.connect(self.applyYellowEffect)
        #   self.horizontalSlider_7.valueChanged.connect(self.applyYellowEffect)
        #
        #   self.hb.clicked.connect(self.applyGrayscale)
        #   self.horizontalSlider_8.valueChanged.connect(self.applyGrayscale)
        #
        #   self.pravos.clicked.connect(self.rotate)
        #   self.pravod.clicked.connect(self.rotate)
        #   self.levod.clicked.connect(self.rotate)
        #   self.image.setPixmap(self.pixmap)
        #   r = QTransform().rotate(self.angle)
        # self.pushButton_10.clicked.connect(self.openImage)
        self.pushButton_9.clicked.connect(self.saveImage)
        # self.push_bd.clicked.connect(ImageProcessor.history_bd)

    def loadImage(self, path):
        self.image = Image.open(path).resize(430, 430)
        self.displayImage()

    # def bd(self):

    def displayImage(self, processed_image=None):
        print(0)
        if processed_image is not None:
            self.image = processed_image

        if self.image is not None:
            print("d")
            qImg = QImage(self.image.tobytes("raw", "RGBA"), self.image.width, self.image.height,
                          QImage.Format_RGBA8888)
            pixmap = QPixmap.fromImage(qImg).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
            self.izobr.setPixmap(pixmap)  # Убрали self.ui.

    def adjustBrightness(self):
        value = self.horizontalSlider.value() / 50.0
        if self.image is not None:
            enhanced = ImageEnhance.Brightness(self.image)
            adjusted_image = enhanced.enhance(value)
            self.addToHistory(f'Adjusted Brightness: {value}')
            self.displayImage(adjusted_image)

    def applyGrayscale(self):
        if self.image is not None:
            grayscale_image = self.image.convert("L")
            self.addToHistory('Applied Grayscale Effect')
            self.displayImage(grayscale_image)

    def blurImage(self):
        kernel_size = self.horizontalSlider_2.value()
        if self.image is not None:
            blurred_image = self.image.filter(ImageFilter.GaussianBlur(radius=kernel_size / 2))
            self.addToHistory(f'Applied Blur: Kernel Size {kernel_size}')
            self.displayImage(blurred_image)

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
                ImageProcessor.tec_tame = datetime.now()
                ImageProcessor.difference = 'сепея'
        except Exception as e:
            print(e)

    def applySepias(self, value):
        try:
            transp = int(self.horizontalSlider_4.value())
            img = Image.open(self.new_file_name)
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

    def channel(self):

        self.curr_image = self.orig_image.copy()
        x, y = self.curr_image.size().width(), self.curr_image.size().height()

        for i in range(x):
            for j in range(y):
                yellow, hb, blue, _ = self.curr_image.pixelColor(i, j).getRgb()

        r = QTransform().rotate(self.angle)
        self.curr_image = self.curr_image.transformed(r)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.izobr.setPixmap(self.pixmap)
        self.loadImage(self.image_path)

    def applyCyanotype(self):
        if self.image is not None:
            cyanotype_image = ImageOps.colorize(self.image.convert("L"), "#003366", "#99CCFF")
            self.addToHistory('Applied Cyanotype Effect')
            self.displayImage(cyanotype_image)

    def applyNegative(self):
        if self.image is not None:
            negative_image = ImageOps.invert(self.image.convert("RGB"))
            self.addToHistory('Applied Negative Effect')
            self.displayImage(negative_image)

    def applyYellowEffect(self):
        if self.image is not None:
            yellow_image = ImageOps.colorize(self.image.convert("L"), "#FFFF00", "#FFFF99")
            self.image = yellow_image

    # def nefative(self):
    #     try:
    #         with Image.open(self.new_file_name) as im:
    #             pix = im.load()
    #             draw = ImageDraw.Draw(im)
    #             width = im.size[0]
    #             height = im.size[1]
    #             for i in range(width):
    #                 for j in range(height):
    #                     a = pix[i, j][0]
    #                     b = pix[i, j][1]
    #                     c = pix[i, j][2]
    #                     draw.point((i, j), (255 - a, 255 - b, 255 - c))
    #             img.save(self.new_file_name)
    #             self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
    #             self.izobr.setPixmap(self.pixmap)
    #
    #     except Exception as e:
    #     print(e)

    def saveImage(self):
        print(0)

        img = Image.open(self.new_file_name)
        img.save(QFileDialog.getSaveFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0])

    def rotate(self):
        with Image.open(self.new_file_name) as im:

            if self.sender() is self.pravod:
                self.image = im.rotate(90)
                self.difference = 'поврот на 90 влево'

            if self.sender() is self.pravos:
                self.image = im.rotate(180)
                self.difference = 'поврот на 90 влево'
            if self.sender() is self.levod:
                self.image = im.rotate(270)
                self.difference = 'поврот на 90 влево'
            self.image.save(self.new_file_name)
            self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
            ImageProcessor.history_bd(datetime.now(), self.difference)



    def open_second_form(self):
        self.second_form = SecondForm(self, "Данные для второй формы")
        self.second_form.show()





class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()
        self.con = sqlite3.connect("db.sqlite")
        self.filter_bd()
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

    def history_bd(self):
        try:
            self.cursor = self.con.cursor()
            self.new_operation = (f'''INSERT
            INTO
            history(time, operation)
            VALUES("{ImageProcessor.tec_tame}", "{ImageProcessor.difference})"''')
            try:
                result = self.cur.execute(self.new_operation).fetchall()
                self.tableWidget_2.setRowCount(len(result))
                self.tableWidget_2.setColumnCount(len(result[0]))
                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))
            except Exception as e:
                print(e)
            self.con.commit()
            self.cursor.close()

        except Exception as e:
            print(e)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessor()
    window.show()
    sys.exit(app.exec_())
