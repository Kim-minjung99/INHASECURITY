# -*- coding: utf-8 -*-
import threading
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from basics import *

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap



login_Gui = '/home/pi/INHASECURITY-main/login.ui'

form_1, base_1 = uic.loadUiType(login_Gui)

class login(form_1,base_1): #MainDialog(QDialog)는 디자이너 위젯을 확인하고 제일 큰 메인 윈도우의 유형과 이름을 확인해야한다.(이름(유형))
    def __init__(self):
        QDialog.__init__(self, None)
        super(base_1, self).__init__()
        #self.ui = uic.loadUi(login_Gui,self)
        lock.acquire()
        self.setupUi(self)

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("cctv.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(200)
        self.cctvlogo.setPixmap(self.qPixmapFileVar)

        self.cctvlogo.setPixmap(self.qPixmapFileVar)
        self.pushButton.clicked.connect(self.loginconfirm)
        self.pushButton_2.clicked.connect(self.cancelclick)
        lock.release()

    def cancelclick(self):
        print(self.lineEdit.clear())
        print(self.lineEdit_2.clear())

    #메인 윈도우창과 다이어로그의 상호작용으로 ui창 전환
    def loginconfirm(self):
        if (self.lineEdit.text() == 'admin') and (self.lineEdit_2.text() == 'admin'):
            self.ui = Mozaic()
            self.ui.show()
            self.close()

        else:

            QtWidgets.QMessageBox.critical(self, 'Notion', '로그인 실패')


if __name__ == "__main__":
    lock=threading.Lock()
    my_thread=threading.Thread()
    my_thread.start()
    
    app = QApplication(sys.argv)
    main_dialog = login() #여기는 메인윈도우의 이름을 적어넣어야한다.
    main_dialog.show()
    my_thread.join()
    print("Login Thread is finished")
    app.exec_()
