import os
import random
import sys

import pygame
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Top(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

app = QApplication(sys.argv)
Display = Top()
Display = TopWindwos()
Display.setFixedSize(900,600)
Display.show()
sys.exit(app.exec_())




#https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247493477&idx=1&sn=33bc854700d6bbdc1f0247e0a10bd136&chksm=978b70aaa0fcf9bcf3231d9a5e151ff72f06581a283da6a28b72d5f1d3cce7f6415c81245456&scene=0&xtrack=1&key=f0e5b32222e59dc566d6c4463fa770f7406122e047cca649ca2be6c59f082bb3103542d5ab018990e30a85976bb7866ede6bbb4156a9050dbc77f4f6be689fad8000f47192ea4befbabb28116323d471&ascene=14&uin=NjQ2NTk5MjIx&devicetype=Windows+10&version=62080079&lang=zh_CN&exportkey=AZ5ZmdVHaZHwxI%2FEiIjLN2k%3D&pass_ticket=K5xKBEBbjEk%2FIviSE%2BBNBtXRuRyis%2BnslQKSe2rbEk6%2BZhRm7%2BnlNtmIV3wG4JbG