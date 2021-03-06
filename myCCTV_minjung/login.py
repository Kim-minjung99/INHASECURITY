# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 434)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cctv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cctvlogo = QtWidgets.QLabel(self.centralwidget)
        self.cctvlogo.setGeometry(QtCore.QRect(130, 20, 271, 81))
        self.cctvlogo.setText("")
        self.cctvlogo.setObjectName("cctvlogo")
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("cctv.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(300)

        self.cctvlogo.setPixmap(self.qPixmapFileVar)


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 100, 401, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(40)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(280, 270, 171, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginconfirm)

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancelclick)

        self.horizontalLayout_6.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "     ID"))
        self.label.setText(_translate("MainWindow", "????????????"))
        self.pushButton.setText(_translate("MainWindow", "?????????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????"))

    def cancelclick(self):
        print(self.lineEdit.clear())
        print(self.lineEdit_2.clear())

    def loginconfirm(self):

        if (self.lineEdit.text() == "admin") and (self.lineEdit_2.text() == "admin"):
            {
                QtWidgets.QMessageBox.information(self,'Notion','????????? ??????')
            }
        else:
            {
                QtWidgets.QMessageBox.critical(self, 'Notion', '????????? ??????')
            }


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
