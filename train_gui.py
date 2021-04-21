import sys
from main_window import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ReLuTrainer import *


'''This window is for when File->Train is clicked'''

class train_Model_Window(QWidget):
    last_Epoch_Num = 2

    def __init__(self):
        super().__init__()
        self.init_UI()
        self.thread_pool = QThreadPool()

    def init_UI(self):
        self.setWindowTitle('Handwriting Training')
        self.show()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,500,25)
        self.pbar.setValue(0)
        
        self.timer = QBasicTimer()
        # self.step = display_Percentage()            

        # self.timer.timeout.connect(self.handleTimer)
        '''Slider to choose number of epoch's'''
        self.epoch_Slider = QSlider(Qt.Horizontal, self)
        self.epoch_Slider.setGeometry(30, 40, 200, 30)
        self.epoch_Slider.setRange(2, 20)
        self.epoch_Slider.valueChanged[int].connect(self.update_Slider_Label)
        self.slider_Label = QLabel('2', self)
        self.slider_Label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.slider_Label.setMinimumWidth(80)

        self.pbar.show() 

        self.train_Btn = QPushButton('&Train',self)
        self.train_Btn.clicked.connect(self.do_Action)
        self.train_Btn.clicked.connect(self.worker_Thread)
        self.train_Btn.show()

        self.results = QLabel("")
        
        # self.cancel_Train = QPushButton('&Cancel Training', self)
        # self.cancel_Train.clicked.connect(stop_Training)
        # self.cancel_Train.show()

        train_win_Layout = QtWidgets.QGridLayout()
        train_win_Layout.addWidget(self.train_Btn, 0, 0, Qt.AlignLeft)
        train_win_Layout.addWidget(self.results, 0, 1, Qt.AlignRight)
        # train_win_Layout.addWidget(self.epoch_Slider, 1, 0)
        # train_win_Layout.addWidget(self.slider_Label, 1, 1)
        # train_win_Layout.addWidget(self.cancelTrain, 1, 0)
        train_win_Layout.addWidget(self.pbar, 2, 0)

        self.setLayout(train_win_Layout)
        #self.train_Btn.clicked.connect()

    def update_Slider_Label(self, value):
        print(value)
        self.slider_Label.setText(str(value))
        # self.worker.last_Epoch_Num = value

    def timer_Event(self, e):
        percentage = display_Percentage()
        if percentage >= 100  or train_Status():
            self.timer.stop()
            self.results = QLabel("Finished Training Model")
            self.pbar.setValue(100)
            return
        self.pbar.setValue(int(percentage))

    def do_Action(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(10, self)
    
    def worker_Thread(self):
        worker = Worker()
        # self.worker_signals = ThreadSignals()
        # self.worker = TestWorker(testInput(1, self.last_Epoch_Num))
        self.thread_pool.start(worker)

        


'''making another thread'''
class Worker(QRunnable):
    last_Epoch_Num = 2

    @pyqtSlot()
    def run(self):
        print('hi')
        '''Remove if it doesn't work'''
        run_Status = True

        # test_Input(1, self.last_Epoch_Num)
        test_Input(1, 5)

        '''Remove if it doesn't work'''
        if run_Status = False:
            break

    '''Remove if it doesn't work'''
    def cancel_Train(self):
        self.run_Status = False
'''Remove if it doesn't work'''
class WorkerSignals(QObject):
    progress = pyqtSignal(int)

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


