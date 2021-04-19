import sys
from main_window import *
from PyQt5.QtWidgets import *
from ReLuTrainer import *


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

        self.trainBtn = QPushButton('&Train',self)
        self.trainBtn.clicked.connect(testInput)
        self.trainBtn.show()

        # self.cancelTrain = QPushButton('&Cancel Training', self)
        # self.cancelTrain.clicked.connect(stopTraining)
        # self.cancelTrain.show()

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(self.trainBtn, 0, 0)
        # gridLayout.addWidget(self.cancelTrain, 1, 0)
        gridLayout.addWidget(self.pbar, 1, 0)

        self.setLayout(gridLayout)
        #self.trainBtn.clicked.connect()







    