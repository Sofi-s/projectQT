import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QSlider, QVBoxLayout, QWidget, QFileDialog, QLabel, \
    QTableWidgetItem,QCommandLinkButton,QShortcut
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb, QTransform, QMouseEvent,QKeySequence
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageEnhance
from pillow_lut import rgb_color_enhance
from PIL.ImageFilter import Color3DLUT, RankFilter, MedianFilter, MinFilter, MaxFilter
import sqlite3
import csv
from PIL import Image

simg = Image.open('cat.jpg')
#
# dimg = simg.filter(MinFilter(size=9))
# dimg.save("x.jpg")
#
# dimg = simg.filter(MedianFilter(size=9))
# dimg.save("x1.jpg")
#
dimg = simg.filter(MaxFilter(size=7))
dimg.save("x.jpg")