from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
import random
import pygame

class Top(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

app = QApplication(sys.argv)
Display = Top()
#Display = TopWindow()
Display.setFixedSize(900,600)
Display.show()
sys.exit(app.exec_())

self.setWindowTitle("消灭病毒小游戏")
self.setWindowIcon(QIcon("图标.jpg"))

