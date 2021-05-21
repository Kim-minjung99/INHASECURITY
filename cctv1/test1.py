import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("capston.ui")[0]

class Ui_MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.btn_clicked1)
        self.pushButton_14.clicked.connect(self.btn_clicked2)
        self.pushButton.clicked.connect(self.btn_clicked3)
        self.pushButton_6.clicked.connect(self.btn_clicked4)
    def btn_clicked1(self):
        filename = QFileDialog.getOpenFileName()
        self.label_5.setText(filename[0])

    def btn_clicked2(self):
        filename = QFileDialog.getOpenFileName()
        self.label_6.setText(filename[0])

    def btn_clicked3(self):
        filename = QFileDialog.getOpenFileName()
        self.label_7.setText(filename[0])

    def btn_clicked4(self):
        filename = QFileDialog.getOpenFileName()
        self.label_8.setText(filename[0])

    def textEdit(self):
        self.textEdit=QTextEdit(self)


    def filedialog_open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '',
                                                'All File(*)')
        if fname[0]:
             # 튜플 데이터에서 첫 번째 인자 값이 주소이다.
            self.pathLabel.setText(fname[0])
            print('filepath : ', fname[0])
            print('filesort : ', fname[1])

            # 텍스트 파일 내용 읽기
            f = open(fname[0], 'r', encoding='UTF8')  # Path 정보로 파일을 읽는다.
            with f:
                data = f.read()
            self.textEdit.setText(data)
        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Ui_MainWindow()
    myWindow.show()
    app.exec_()