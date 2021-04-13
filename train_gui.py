import sys
from PyQt5.QtWidgets import *

'''This window is for when File->Train is clicked'''

class trainModelWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Handwriting Training')
        self.show()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,500,25)


        self.pbar.show() 




    