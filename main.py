import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QSlider, QVBoxLayout, QWidget, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb, QTransform
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore
from PIL import Image, ImageEnhance, ImageFilter, ImageOps


class ImageProcessor(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi('photoshop2.ui', self)
        self.image = None
        self.image_path = None
        self.filename = self.image_path
        self.orig_image = QImage(self.filename)
        self.curr_image = self.orig_image.copy()
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.izobr.setPixmap(self.pixmap)
        self.pravos.clicked.connect(self.rotate)
        self.levod.clicked.connect(self.rotate)
        self.pravod.clicked.connect(self.rotate)
        self.izobr.setPixmap(self.pixmap)
        self.izobr.setStyleSheet("background-color: gray;")
        self.angle = 0
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setValue(255)
        #self.slider.valueChanged.connect(self.visibility)
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
        #   self.sepeia.clicked.connect(self.applySepia)
        #   self.horizontalSlider_4.valueChanged.connect(self.applySepia)
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
        self.pushButton_10.clicked.connect(self.openImage)

    #   self.pushButton_9.clicked.connect(self.saveImage)

    def loadImage(self, path):
        self.image = Image.open(path)
        self.displayImage()

    def displayImage(self, processed_image=None):
        if processed_image is not None:
            self.image = processed_image

        if self.image is not None:
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
        print(value)
        try:
            if self.image:
                #transp = int(value)
                transp = int(self.horizontalSlider_3.value())
                # img = (self.file_name)
                img = Image.open(self.image_path)
                img = img.convert('RGBA')
                img.putalpha(transp)
                self.pixmap = QPixmap(self.image_path)
                self.image = self.pixmap


        except Exception as e:
            print(e)

        # def prozrachnost(self, value):
        #     try:
        #         transp = int(self.alpha.value())
        #         img = Image.open(self.file_name)
        #         img.putalpha(transp)
        #         img.save(self.new_file_name)
        #         self.pixmap = QPixmap(self.new_file_name)
        #         self.gogl.setPixmap(self.pixmap)
        #     except Exception as e:
        #         print(e)

    #
    # def prozrachnost(self, value):
    #     try:
    #         transp = int(self.alpha.value())
    #         img = Image.open(self.file_name)
    #         img.putalpha(transp)
    #         img.save(self.new_file_name)
    #         self.pixmap = QPixmap(self.new_file_name)
    #         self.gogl.setPixmap(self.pixmap)
    #     except Exception as e:
    #         print(e)

    def applySepia(self):
        if self.image is not None:
            sepia_image = ImageOps.colorize(self.image.convert("L"), "#704214", "#C0A080")
            self.addToHistory('Applied Sepia Effect')

            self.image_path = self.displayImage(sepia_image)

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

    def openImage(self):
        options = QFileDialog.Options()

        self.image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                         "Images (*.png *.jpg *.bmp *.jpeg *.gif *.tiff);;All Files (*)",
                                                         options=options)
        if self.image_path:
            self.loadImage(self.image_path)

    def applyYellowEffect(self):
        if self.image is not None:
            yellow_image = ImageOps.colorize(self.image.convert("L"), "#FFFF00", "#FFFF99")
            self.image = yellow_image

    def saveImage(self):
        if self.image is not None:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Image File", "",
                                                       "Images (*.png *.jpg *.bmp *.jpeg *.gif *.tiff);;All Files (*)",
                                                       options=options)
            if file_path:
                self.image.save(file_path)

    def rotate(self):
        if self.sender() is self.pravod:
            self.angle += 90
            rotation_angle = 90
        elif self.sender() is self.levod:
            self.angle -= 90
            rotation_angle = -90
        elif self.sender() is self.pravos:
            self.angle -= 180
            rotation_angle = -180
        else:
            rotation_angle = 0

        self.angle += rotation_angle
        self.angle %= 360
        r = QTransform().rotate(self.angle)
        self.curr_image = self.curr_image.transformed(r)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.izobr.setPixmap(self.pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessor()
    window.show()
    sys.exit(app.exec_())
