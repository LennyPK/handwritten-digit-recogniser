import sys
from PyQt5.QtWidgets import *

'''This window is for when File->Train is clicked'''

class trainModelWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Handwriting Training')
        self.show()


    