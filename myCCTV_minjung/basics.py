# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPalette
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMessageBox

Gui = 'C:/Users/김민정/PycharmProjects/pythonProject/allui.ui'

class Mozaic(QMainWindow):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(Gui,self)

        self.PlayButton.clicked.connect(self.PlayButtonM)
        # self.StopMomentButton.clicked.connect(self.StopMomentButtonM)
        # self.PauseButton.clicked.connect(self.PauseButtonM)
        # self.pushButton.clicked.connect(self.pushButtonM)
        # self.pushButton_2.clicked.connect(self.pushButton_2M)
        self.HelpButton1.clicked.connect(self.HelpButton1M)
        self.HelpButton2.clicked.connect(self.HelpButton2M)
        self.HelpButton3.clicked.connect(self.HelpButton3M)
        # self.horizontalSlider.sliderMoved.connect(self.barChanged)
        # self.listWidget.itemDoubleClicked.connect(self.dbClickList)
        #self.LoadingButton.clicked.connect(self.LoadingButtonM)
        self.pushButton.clicked.connect(self.AddbuttonM)
        self.pushButton_2.clicked.connect(self.clickDel)

        self.HelpButton1.setStyleSheet('image:url(HELP1.png)')
        self.HelpButton2.setStyleSheet('image:url(HELP2.png)')
        self.HelpButton3.setStyleSheet('image:url(HELP3.png)')
        self.PlayButton.setStyleSheet('image:url(재생.png)')
        self.StopMomentButton.setStyleSheet('image:url(일시정지.png)')
        self.PauseButton.setStyleSheet('image:url(중지.png)')

        self.mediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.view = QVideoWidget()
        self.view.setObjectName("view")
        self.mediaplayer.setVideoOutput(self.view)




    def PlayButtonM(self):
        # self.mediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        #
        # view = QVideoWidget()
        # view.setObjectName("view")
        # self.mediaplayer.setVideoOutput(view)

        self.mediaplayer.play()



    def AddbuttonM(self):
        files, ext = QFileDialog.getOpenFileName(self, "모자이크 동영상 선택",
                ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)") #동영상 불러오기
        if files:
            #cnt = len(files)
            row = self.listWidget.count()

            #for i in range(row, row + cnt): # i=cnt
            self.listWidget.addItem(files)
            self.listWidget.setCurrentRow(row)

            #self.listWidget.addItem(files[0])
            #self.listWidget.setCurrentRow(0)

    #            self.mediaPlayer.addMedia(files)

    def clickDel(self):
        row = self.listWidget.currentRow()
        self.listWidget.takeItem(row)

    def HelpButton1M(self):
        QMessageBox.information(self,"Starting Initializing 도움말","본 Starting Initializing 서비스는 고객의 얼굴을 인식하여, "
                                             "미디어 상의 고객의 얼굴을 찾고자 Dataset을 마련하는 과정입니다.\n"
                                             "\n"
                                             "앞서 2, 3단계를 시작하기 전에 본 기기의 카메라에 얼굴을 댄 후, "
                                             "별도의 지시사항이 나오기 전에 대기하여 주십시오.\n"
                                                                 "\n")

    def HelpButton2M(self):
        QMessageBox.information(self, "Training 도움말", "본 Training 서비스는 1단계에서 인식한 고객의 얼굴을 바탕으로 생성된 "
                                               "Dataset을 이용하여, "
                                               "Mozaic 프로그램 상에 인식하는 과정입니다.\n"
                                               "\n"
                                               "앞서 3단계를 시작하기 전 별도의 지시사항이 나오기 전까지 대기하여 주십시오.\n"
                                                      "\n")

    def HelpButton3M(self):
        QMessageBox.information(self, "Confirm Video 도움말", "본 Confirm Video 서비스는 1,2단계에서 완료한 고객의 얼굴 인식을 바탕으로 영상처리하여"
                                               "실제 동영상을 확인하는 과정입니다.\n"
                                               "\n"
                                               "ADD버튼과 DELETE버튼을 이용하여 시청하고자 하는 영상을 리스트상에 추가 및 제거할 수 "
                                               "있으며, 영상의 배속을 조절할 수 있습니다.\n"
                                               "\n"
                                               "또한 영상을 재생, 중지, 일시 정지시킬수 도 있습니다.\n"
                                                           "\n")

app = QApplication(sys.argv)
main_dialog = Mozaic()
main_dialog.show()
app.exec_()