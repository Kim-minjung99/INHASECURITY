import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import uic

#load both ui file
uifile_1 = 'login.ui'
form_1, base_1 = uic.loadUiType(uifile_1)
print(base_1)
print(form_1)

uifile_2 = 'allui.ui'
form_2, base_2 = uic.loadUiType(uifile_2)
print(base_2)
print(form_2)

class Example(base_1, form_1):
    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.change)

    def change(self):
        self.main = MainPage()
        self.main.show()
        self.close()

class MainPage(base_2, form_2):
    def __init__(self):
        super(base_2, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())