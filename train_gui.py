import sys
from main_window import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ReLuTrainer import *


'''This window is for when File->Train is clicked'''

class trainModelWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.threadpool = QThreadPool()

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
        # self.trainBtn.clicked.connect(self.doAction)
        self.trainBtn.clicked.connect(self.workerThread)
        self.trainBtn.show()

        self.results = QLabel("")
        
        # self.cancelTrain = QPushButton('&Cancel Training', self)
        # self.cancelTrain.clicked.connect(stopTraining)
        # self.cancelTrain.show()

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(self.trainBtn, 0, 0, Qt.AlignLeft)
        gridLayout.addWidget(self.results, 0, 1, Qt.AlignRight)
        # gridLayout.addWidget(self.cancelTrain, 1, 0)
        gridLayout.addWidget(self.pbar, 1, 0)

        self.setLayout(gridLayout)
        #self.trainBtn.clicked.connect()

    def timerEvent(self, e):
        percentage = displayPercentage()
        if percentage >= 100  or trainStatus():
            self.timer.stop()
            self.results = QLabel("Finished Training Model")
            return
        self.pbar.setValue(int(percentage))

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(10, self)
    
    def workerThread(self):
        worker = Worker()
        self.threadpool.start(worker)


# Step 1: Create a worker class
class Worker(QRunnable):

    @pyqtSlot()
    def run(self):
        testInput(1, 2)
