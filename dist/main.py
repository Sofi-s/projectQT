import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QSlider, QVBoxLayout, QWidget, QFileDialog, QLabel, \
    QTableWidgetItem, QCommandLinkButton, QShortcut
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb, QTransform, QMouseEvent, QKeySequence
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageEnhance
from pillow_lut import rgb_color_enhance
from PIL.ImageFilter import Color3DLUT, RankFilter, MedianFilter, MinFilter, MaxFilter
import sqlite3
import datetime


class ImageProcessor(QDialog):

    difference = []

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
        self.zerc.clicked.connect(self.z)
        self.izobr.setPixmap(self.pixmap)
        self.izobr.setStyleSheet("background-color: white;")
        self.angle = 0
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setValue(255)
        self.horizontalSlider_4.setMinimum(0)
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setValue(0)
        self.horizontalSlider_2.setValue(0)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(150)
        self.push_bd.clicked.connect(self.open_second_form)
        self.comBY_yvel.clicked.connect(lambda: self.yark_yvelich_1)
        self.yarkost.clicked.connect(self.adjustBrightness)
        self.pushBu_orig.clicked.connect(self.orig_im)
        tec_tame = 0
        # self.difference = []
        self.horizontalSlider_2.valueChanged[int].connect(self.razmatie)
        self.horizontalSlider_3.valueChanged[int].connect(self.adjustTransparency)
        self.horizontalSlider_4.valueChanged[int].connect(self.applySepias)
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
        self.pushButton_9.clicked.connect(self.saveImage)
        self.con = sqlite3.connect("db.sqlite")
        self.query = """DELETE from history"""
        print(self.query)
        self.cursor = self.con.cursor()
        self.cursor.execute(self.query)
        self.con.commit()
        shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        shortcut.activated.connect(self.saveImage)
        self.comBY_yvel.clicked.connect(self.increaseBrightness)
        self.contr_yvelich.clicked.connect(self.contrast_f)
        self.recz_yvel.clicked.connect(self.inrezcost)
        self.but_lychi.clicked.connect(self.luchi_f)
        self.but_snow.clicked.connect(self.snow_f)
        self.b_night.clicked.connect(self.night_f)
        self.b_summer.clicked.connect(self.summer_f)
        self.b_H2O.clicked.connect(self.H2O_f)
        self.b_gold.clicked.connect(self.gold_f)
        self.b_dreems.clicked.connect(self.dreems_f)
        self.but_contur.clicked.connect(self.contur_f1)
        self.but_contur1.clicked.connect(self.contur_f)
        self.but_contur2.clicked.connect(self.contur_f2)
        self.but_contur3.clicked.connect(self.contur_f3)
        self.contrast.clicked.connect(self.contrast_yvelich_1)


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
                self.factor = 2
                self.im_output = self.enhancer.enhance(self.factor)
                self.im_output.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('transparency filter')
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
            ImageProcessor.tec_tame = datetime.datetime.now()
            ImageProcessor.difference.append('transparency')


        except Exception as e:
            print(e)

    def razmatie(self, value):
        try:
            transp = int(self.horizontalSlider_4.value())
            img = Image.open(self.new_file_name)
            img = img.filter(ImageFilter.BLUR)  # использование ImageFilter.BLUR для размытия
            img.save(self.new_file_name)
            self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
            self.izobr.setPixmap(self.pixmap)
            ImageProcessor.tec_tame = datetime.datetime.now()
            ImageProcessor.difference.append('razmitie')
        except Exception as e:
            print(e)

    def increaseBrightness(self):
        try:
            self.adjustBrightness()
            self.factor += 0.2
            ImageProcessor.tec_tame = datetime.datetime.now()
            ImageProcessor.difference.append('Brightness')
        except Exception as e:
            print(e)

    def yark_yvelich_1(self):
        try:
            with Image.open(self.new_file_name) as im:
                self.enhancer = ImageEnhance.Brightness(im)
                self.factor = 1
                self.comBY_yvel.clicked.connect(lambda: self.comBY_yvel(self.factor))
                self.im_output = self.enhancer.enhance(self.factor)
                self.im_output.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)

    def contrast_f(self):
        try:
            self.adjustBrightness()
            self.factor += 0.2
            ImageProcessor.tec_tame = datetime.datetime.now()
            ImageProcessor.difference.append('contrast filter')
        except Exception as e:
            print(e)

    def contrast_yvelich_1(self):
        try:
            with Image.open(self.new_file_name) as im:
                self.enhancer = ImageEnhance.Contrast(im)
                self.factor = 1
                self.comBY_yvel.clicked.connect(lambda: self.contr_yvelich(self.factor))
                self.im_output = self.enhancer.enhance(self.factor)
                self.im_output.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)

    def rezcost(self):
        try:
            with Image.open(self.new_file_name) as im:
                enhancer = ImageEnhance.Sharpness(im)
                factor = 1
                self.comBY_yvel.clicked.connect(lambda: self.recz_yvel(self.factor))
                self.im_s_1 = enhancer.enhance(factor)
                self.im_s_1.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)
    def inrezcost(self):
        try:
            self.adjustBrightness()
            self.factor += 0.2
            ImageProcessor.tec_tame = datetime.datetime.now()
            ImageProcessor.difference.append('rezcost')
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
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('sepea filter')
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
            ImageProcessor.tec_tame = datetime.datetime.now()
            ImageProcessor.difference.append('sepea slaider filter')
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
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('gray filter')
        except Exception as e:
            print(e)

    def orig_im(self):
        try:
            with Image.open(self.filename) as im:
                im.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('open first filter')
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
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('red filter')
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
                ImageProcessor.difference.append('blue filter')
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
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('green filter')
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
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('negative')

        except Exception as e:
            print(e)

    def H2O_f(self):
        try:
            with Image.open(self.new_file_name) as img:
                self.dimg = img.filter(RankFilter(size=9, rank=3))
                self.dimg.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('H2O')
        except Exception as e:
            print(e)

    def saveImage(self):
        print(0)
        img = Image.open(self.new_file_name)
        img.save(QFileDialog.getSaveFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0])

    def rotate(self):
        im = Image.open(self.new_file_name)
        try:
            if self.sender() is self.pravod:
                self.image = im.rotate(90)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('90 right')
            if self.sender() is self.pravos:
                self.image = im.rotate(180)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('180')
            if self.sender() is self.levod:
                self.image = im.rotate(270)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('90 left')
            self.image.save(self.new_file_name)
            self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
            self.izobr.setPixmap(self.pixmap)
        except Exception as e:
            print(e)

    def luchi_f(self):
        try:
            with Image.open(self.new_file_name) as img:
                def transform(r, g, b):
                    r, g, b = (max(r, g, b), g, min(r, g, b))
                    avg_v = r * 0.2126 + g * 0.7152 + b * 0.0722
                    r += (r - avg_v) * 0.6
                    g += (g - avg_v) * 0.6
                    b += (b - avg_v) * 0.6
                    return r, g, b

                self.lut = Color3DLUT.generate(17, transform)
                self.filtered_img = img.filter(self.lut)
                self.filtered_img.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('morhihg')
        except Exception as e:
            print(e)

    def night_f(self):
        try:
            with Image.open(self.new_file_name) as img:
                self.table = [(0, 1, 1), (0, 0, 1), (0, 0, 0), (0, 0, 1),
                              (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
                self.lut = Color3DLUT(2, self.table)
                self.filtered_img = img.filter(self.lut)
                self.filtered_img.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('night')
        except Exception as e:
            print(e)

    def snow_f(self):
        try:
            with Image.open(self.new_file_name) as img:
                self.lut = rgb_color_enhance(11, exposure=1, contrast=0.3, vibrance=-0.2, warmth=0.3)
                self.filtered_img = img.filter(self.lut)
                self.filtered_img.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('snow')
        except Exception as e:
            print(e)

    def gold_f(self):
        try:
            with Image.open(self.new_file_name) as img:
                self.dimg = img.filter(MaxFilter(size=7))
                self.dimg.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('gold')
        except Exception as e:
            print(e)

    def summer_f(self):
        try:
            with Image.open(self.new_file_name) as img:
                self.lut = rgb_color_enhance(11, exposure=0.1, contrast=0.2, vibrance=0.2, warmth=0.57)
                self.filtered_img = img.filter(self.lut)
                self.filtered_img.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('summer')
        except Exception as e:
            print(e)

    def z(self):
        with Image.open(self.new_file_name) as im:
            try:
                self.image = im.transpose(Image.FLIP_LEFT_RIGHT)
                self.image.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('zerkalo')

            except Exception as e:
                print(e)

    def contur_f(self):
        try:
            with Image.open(self.filename) as im:
                self.img_gray = im.convert("L")
                self.edges = self.img_gray.filter(ImageFilter.FIND_EDGES)
                self.edges.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('contur pro')
        except Exception as e:
            print(e)

    def contur_f1(self):
        try:
            with Image.open(self.filename) as im:
                self.img_gray = im.convert("L")
                self.img_gray_smooth = self.img_gray.filter(ImageFilter.SMOOTH)
                self.edges_smooth = self.img_gray_smooth.filter(ImageFilter.FIND_EDGES)
                self.edges_smooth.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('contur')
        except Exception as e:
            print(e)

    def contur_f2(self):
        try:
            with Image.open(self.filename) as im:
                self.img_gray = im.convert("L")
                self.img_gray_smooth = self.img_gray.filter(ImageFilter.SMOOTH)
                self.emboss = self.img_gray_smooth.filter(ImageFilter.EMBOSS)
                self.emboss.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('white-black')
        except Exception as e:
            print(e)

    def contur_f3(self):
        try:
            with Image.open(self.filename) as im:
                img_cat_gray = im.convert("L")
                threshold = 100
                self.img_cat_threshold = img_cat_gray.point(
                    lambda x: 255 if x > threshold else 0)
                self.img_cat_threshold.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('tisnenie')

        except Exception as e:
            print(e)

    def dreems_f(self):
        try:
            with Image.open(self.new_file_name) as img:
                self.table = [(0, 1, 1), (1, 0, 1), (0, 1, 0), (1, 0, 0),
                              (0, 1, 0), (1, 1, 0), (1, 1, 0), (0, 0, 0)]
                self.lut = Color3DLUT(2, self.table)
                self.filtered_img = img.filter(self.lut)
                self.filtered_img.save(self.new_file_name)
                self.pixmap = QPixmap(self.new_file_name).scaled(430, 430, QtCore.Qt.KeepAspectRatio)
                self.izobr.setPixmap(self.pixmap)
                ImageProcessor.tec_tame = datetime.datetime.now()
                ImageProcessor.difference.append('dreems')

        except Exception as e:
            print(e)

    def open_second_form(self):
        self.second_form = SecondForm(self, "Данные для второй формы")
        self.second_form.show()

    def eventFilter(self, obj, event):
        if event.type() == event.ShortcutOverride:
            return True
        return super().eventFilter(obj, event)
class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()
        self.con = sqlite3.connect("db.sqlite")
        self.filter_bd()

        self.loadTable('images2.csv')
        self.history_bd()
        self.pushButton_alf.clicked.connect(self.sortirovka)

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
        try:
            for i in ImageProcessor.difference:
                self.cursor = self.con.cursor()
                self.query = f'''INSERT
                            INTO history(time, operation)
                            VALUES('{ImageProcessor.tec_tame}', '{i}')'''
                self.new_operation = self.query
                self.cur.execute(self.query)
            try:
                result = self.cur.execute("Select * from history").fetchall()
                self.tableWidget_2.setRowCount(len(result))
                self.tableWidget_2.setColumnCount(len(result[0]))
                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))
                        self.con.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

    def sortirovka(self):
        try:
            self.cursor = self.con.cursor()
            self.query = (f'''SELECT    time, operation FROM
        history ORDER BY operation''')
            self.new_operation = self.query
            self.cur.execute(self.query)
            print(self.query)
            try:
                print(8)
                # result = self.cur.execute("Select * from history").fetchall()
                result = self.cur.execute(f'''SELECT    time, operation FROM
        history ORDER BY operation''').fetchall()
                self.tableWidget_2.setRowCount(len(result))
                self.tableWidget_2.setColumnCount(len(result[0]))
                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))
                        self.con.commit()
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    print(datetime.datetime.now())
    app = QApplication(sys.argv)
    window = ImageProcessor()
    window.show()
    sys.exit(app.exec_())
