import sys
from main_window import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ReLuTrainer import *
from worker_thread import *

'''This window is for when File -> Train is clicked'''
class trainModelWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        '''setting up threadpool'''
        self.threadpool = QThreadPool()

    def initUI(self):
        self.setWindowTitle('Handwriting Training')
        self.show()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,500,25)
        self.pbar.setValue(0)
        
        self.timer = QBasicTimer()

        self.pbar.show() 

        grid_layout = QtWidgets.QGridLayout()
        grid_layout.addWidget(self.button_group(), 0, 0)
        grid_layout.addWidget(self.pbar, 3, 0)

        self.setLayout(grid_layout)

    def button_group(self):
        groupBox = QGroupBox('Models')
        
        self.train_button_1 = QPushButton('&Model 1\nLow Accuracy',self)
        self.train_button_1.clicked.connect(self.do_action)
        self.train_button_1.clicked.connect(self.model_1_thread)
        self.train_button_1.show()

        self.train_button_2 = QPushButton('&Model 2\nHigher Accuracy',self)
        self.train_button_2.clicked.connect(self.do_action)
        self.train_button_2.clicked.connect(self.model_2_thread)
        self.train_button_2.show()

        self.train_button_3 = QPushButton('&Model 1\nRecommended',self)
        self.train_button_3.clicked.connect(self.do_action)
        self.train_button_3.clicked.connect(self.model_3_thread)
        self.train_button_3.show()

        self.train_button_4 = QPushButton('&Model 1\nHighest Accuracy',self)
        self.train_button_4.clicked.connect(self.do_action)
        self.train_button_4.clicked.connect(self.model_4_thread)
        self.train_button_4.show()

        btnBox = QHBoxLayout()
        btnBox.addWidget(self.train_button_1)
        btnBox.addWidget(self.train_button_2)
        btnBox.addWidget(self.train_button_3)
        btnBox.addWidget(self.train_button_4)

        groupBox.setLayout(btnBox)

        return groupBox

    def timerEvent(self, e):
        percentage = displayPercentage()
        if percentage >= 100  or trainStatus():
            self.timer.stop()
            self.results = QLabel("Finished Training Model")
            self.pbar.setValue(100)
            return
        self.pbar.setValue(int(percentage))

    def do_action(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(10, self)
    
    def model_1_thread(self):
        worker = Worker_1()
        self.threadpool.start(worker)

    def model_2_thread(self):
        worker = Worker_2()
        self.threadpool.start(worker)

    def model_3_thread(self):
        worker = Worker_3()
        self.threadpool.start(worker)

    def model_4_thread(self):
        worker = Worker_4()
        self.threadpool.start(worker)

