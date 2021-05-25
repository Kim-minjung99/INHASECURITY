# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainDialog(QDialog): #MainDialog(QDialog)는 디자이너 위젯을 확인하고 제일 큰 메인 윈도우의 유형과 이름을 확인해야한다.(이름(유형))
    def __init__(self):
        QDialog.__init__(self, None)

app = QApplication(sys.argv)
main_dialog = MainDialog() #여기는 메인윈도우의 이름을 적어넣어야한다.
main_dialog.show()
app.exec_()