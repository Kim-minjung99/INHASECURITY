# -*- coding: utf-8 -*-

import sys
import threading
import logging
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtWidgets import QMessageBox





#로깅 출력 형식 지정
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#사용자 지정 핸들러 선언
class LogStringHandler(logging.Handler):
    def __init__(self, log):
        super(LogStringHandler, self).__init__()
        self.log = log

    def emit(self, record):
        self.log.append(record.asctime + ' -- ' + record.getMessage())

Gui = '/home/pi/INHASECURITY-main/allui.ui'


class Mozaic(QMainWindow):
    def __init__(self, parent=None):
        super(Mozaic, self).__init__(parent)
        QDialog.__init__(self, None)
        #lock.acquire()
        self.ui = uic.loadUi(Gui, self)
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("cctv.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(200)
        self.cctvlogo.setPixmap(self.qPixmapFileVar)

        #self.PlayButton.clicked.connect(self.PlayButtonM)
        self.StopMomentButton.clicked.connect(self.StopMomentButtonM)
        # self.PauseButton.clicked.connect(self.PauseButtonM)
        self.HelpButton1.clicked.connect(self.HelpButton1M)
        self.HelpButton2.clicked.connect(self.HelpButton2M)
        self.HelpButton3.clicked.connect(self.HelpButton3M)

        # self.listWidget.itemDoubleClicked.connect(self.dbClickList)
        self.LoadingButton.clicked.connect(self.LoadingButtonM)
        self.SaveButton.clicked.connect(self.SaveButtonM)
        self.pushButton.clicked.connect(self.AddbuttonM)
        self.pushButton_2.clicked.connect(self.clickDel)
        self.NameButton.clicked.connect(self.NameButtonM)

        #로깅 이벤트 연결
        self.TrainingButton.clicked.connect(self.trainingButtonM)

        #로그 핸들러 로깅화면에 추가하여 출력시키기
        logger = logging.getLogger()
        logger.addHandler(LogStringHandler(self.seeResultTraining))


        self.HelpButton1.setStyleSheet('image:url(HELP1.png)')
        self.HelpButton2.setStyleSheet('image:url(HELP2.png)')
        self.HelpButton3.setStyleSheet('image:url(HELP3.png)')
        self.PlayButton.setStyleSheet('image:url(재생.png)')
        self.StopMomentButton.setStyleSheet('image:url(일시정지.png)')
        #self.PauseButton.setStyleSheet('image:url(중지.png)')

        self.player = QMediaPlayer()
        # self.widget = QVideoWidget()
        self.player.setVideoOutput(self.ui.widget)
        self.ui.PlayButton.clicked.connect(self.PlayButtonM)
        #lock.release()

        #Progress bar
        # 슬라이더 선언
        # self.horizontalSlider.setRange(0, 0)
        # self.horizontalSlider.sliderMoved.connect(self.barChanged)
        # self.player.durationChanged.connect(self.getDuration)
        # self.player.positionChanged.connect(self.getPosition)

    def PlayButtonM(self):
        PlayFile = self.listWidget.currentItem().text()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(PlayFile)))
        self.player.play()

    def StopMomentButtonM(self):
        self.player.pause()

    # def barChanged(self, position):
    #     self.player.setPosition(position)
    #
    # def getDuration(self, duration):
    #     self.horizontalSlider.setRange(0, duration)
    #
    # def getPosition(self,position):
    #     self.positionSlider.setValue(position)


    #여기서부터 로그 출력 기능
    def trainingButtonM(self):
        self.test_logging()

    def test_logging(self):
        logging.error('%s')
        logging.info('%s')
        logging.warning('%s')
        logging.debug('%s')

        #return '로그 출력 완료'

    #여기까지 로그


    #리스트뷰에 영상 추가
    def AddbuttonM(self):
        files, ext = QFileDialog.getOpenFileName(self, "모자이크 동영상 선택",
                                                 ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")  # 동영상 불러오기
        if files:
            # cnt = len(files)
            row = self.listWidget.count()

            # for i in range(row, row + cnt): # i=cnt
            self.listWidget.addItem(files)
            self.listWidget.setCurrentRow(row)
            # self.listWidget.addItem(files[0])
            # self.listWidget.setCurrentRow(0)

    #            self.mediaPlayer.addMedia(files)

    #리스트 뷰에 추가한 동영상 제거
    def clickDel(self):
        row = self.listWidget.currentRow()
        self.listWidget.takeItem(row)

    def NameButtonM(self):  # 이름을 가져와서 저장시키기 아직은 print까지밖에 안됨
        Naming = self.Naming.text()
        print(Naming)

    def LoadingButtonM(self):
        files, ext = QFileDialog.getOpenFileName(self, "모자이크 동영상 선택",
                                                 ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")  # 동영상 불러오기
        if files:
            # cnt = len(files)
            # row = self.listWidget.count()

            # for i in range(row, row + cnt): # i=cnt
            self.VideoLoadpath.setText(files)

    #     files = QFileDialog.getOpenFileName()
    #     self.VideoLoadpath.setText(files[0])

    def SaveButtonM(self):
        files, ext = QFileDialog.getOpenFileName(self, "모자이크 동영상 선택",
                                                  ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")  # 동영상 불러오기
        if files:
            # cnt = len(files)
            # row = self.listWidget.count()

            # for i in range(row, row + cnt): # i=cnt
            self.VideoSavePath.setText(files)

    #     files = QFileDialog.getOpenFileName()
    #     self.VideoLoadpath.setText(files[0])

    def HelpButton1M(self):
        QMessageBox.information(self, "Starting Initializing 도움말", "본 Starting Initializing 서비스는 고객의 얼굴을 인식하여, "
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


if __name__ == "__main__":
    '''
    lock = threading.Lock()
    my_thread = threading.Thread()
    my_thread.start()'''
    
    app = QApplication(sys.argv)
    main_dialog = Mozaic()
    main_dialog.show()
    #my_thread.join()
    #print("Login Thread is finished")
    app.exec_()
