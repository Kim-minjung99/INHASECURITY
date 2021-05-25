# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
#
# form_class = uic.loadUiType("test.ui")[0]
#
# class MyWindow(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MyWindow()
#     myWindow.show()
#     app.exec_()

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("capston.ui")[0]     #UI파일 연결

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    """
    ---------------------------------------------
    이 부분에 시그널을 입력.
    시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수로 작성.
    ---------------------------------------------
    """

if __name__ == "__main__" :

    app = QApplication(sys.argv)    #QApplication : 프로그램을 실행시켜주는 클래스

    myWindow = WindowClass()        #WindowClass의 인스턴스 생성

    myWindow.show()                 #프로그램 화면을 보여주는 코드

    app.exec_()                     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드