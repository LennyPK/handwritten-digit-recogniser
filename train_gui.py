import sys
from main_window import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ReLuTrainer import *
#from test_trainer import *

'''This window is for when File->Train is clicked'''

class trainModelWindow(QWidget):
    lastEpochNum = 2

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
        '''Slider to choose number of epoch's'''
        self.epochSlider = QSlider(Qt.Horizontal, self)
        self.epochSlider.setGeometry(30, 40, 200, 30)
        self.epochSlider.setRange(2, 20)
        self.epochSlider.valueChanged[int].connect(self.updateSliderLabel)
        self.sliderLabel = QLabel('2', self)
        self.sliderLabel.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.sliderLabel.setMinimumWidth(80)

        self.pbar.show() 

        self.trainBtn = QPushButton('&Train',self)
        self.trainBtn.clicked.connect(self.doAction)
        self.trainBtn.clicked.connect(self.workerThread)
        self.trainBtn.show()

        self.results = QLabel("")
        
        # self.cancelTrain = QPushButton('&Cancel Training', self)
        # self.cancelTrain.clicked.connect(stopTraining)
        # self.cancelTrain.show()

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(self.trainBtn, 0, 0, Qt.AlignLeft)
        gridLayout.addWidget(self.results, 0, 1, Qt.AlignRight)
        # gridLayout.addWidget(self.epochSlider, 1, 0)
        # gridLayout.addWidget(self.sliderLabel, 1, 1)
        # gridLayout.addWidget(self.cancelTrain, 1, 0)
        gridLayout.addWidget(self.pbar, 2, 0)

        self.setLayout(gridLayout)

    def updateSliderLabel(self, value):
        print(value)
        self.sliderLabel.setText(str(value))
        # self.worker.lastEpochNum = value

    def timerEvent(self, e):
        percentage = displayPercentage()
        if percentage >= 100  or trainStatus():
            self.timer.stop()
            self.results = QLabel("Finished Training Model")
            self.pbar.setValue(99)
            return
        self.pbar.setValue(int(percentage))

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(10, self)
    
    def workerThread(self):
        worker = Worker()
        # self.worker_signals = ThreadSignals()
        # self.worker = TestWorker(testInput(1, self.lastEpochNum))
        self.threadpool.start(worker)

'''making another thread'''
class Worker(QRunnable):
    lastEpochNum = 2

    @pyqtSlot()
    def run(self):
        # conv_model = Net()
        # train_model(2, conv_model)
        testInput(1,2)

# Maybe change this to worker and the other one above to ThreadSignals or WorkerSignals
# class ThreadSignals(QObject):
#     model_progress = pyqtSignal()
#     finished = pyqtSignal()

# class TestWorker(QRunnable):

#     def __init__(self, fn, *args, **kwargs):
#         super(TestWorker, self).__init__()
#         self.fn = fn
#         self.args = args
#         self.kwargs = kwargs
#         self.signals = ThreadSignals()

#         self.kwargs['cbk_progress'] = self.signals.model_progress

#     @pyqtSlot()
#     def run(self):

#         try:
#             result = self.fn(*self.args, **self.kwargs)
        
#         except:
#             print("didnt work you shit")
#         else:
#             print("meme")
#         finally:
#             self.signals.finished.emit()


