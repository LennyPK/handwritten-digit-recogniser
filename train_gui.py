import sys
from main_window import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer
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
        self.pbar.setValue(0)
        
        self.timer = QBasicTimer()
        # self.step = displayPercentage()            

        # self.timer.timeout.connect(self.handleTimer)

        self.pbar.show() 

        self.trainBtn = QPushButton('&Train',self)
        self.trainBtn.clicked.connect(self.doAction)
        self.trainBtn.clicked.connect(lambda: testInput(1, 4))
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

    def timerEvent(self, e):
        percentage = displayPercentage()
        if percentage >= 99.5:
            self.timer.stop()
            return
        self.pbar.setValue(int(percentage)) 

    def doAction(self):
        
        if self.timer.isActive():
            self.timer.stop()
            # self.btn.setText('Start')
        else:
            self.timer.start(10, self)
            # self.btn.setText('Stop')







    