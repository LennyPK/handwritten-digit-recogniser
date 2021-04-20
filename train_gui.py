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
        # self.trainBtn.clicked.connect(self.doAction)
        self.trainBtn.clicked.connect(lambda: testInput(1, 10))
        self.trainBtn.show()

        self.results = QLabel()
        
        # self.cancelTrain = QPushButton('&Cancel Training', self)
        # self.cancelTrain.clicked.connect(stopTraining)
        # self.cancelTrain.show()

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(self.trainBtn, 0, 0)
        gridLayout.addWidget(self.results, 0, 1)
        # gridLayout.addWidget(self.cancelTrain, 1, 0)
        gridLayout.addWidget(self.pbar, 1, 0)

        self.setLayout(gridLayout)
        #self.trainBtn.clicked.connect()

    def timerEvent(self, e):
        percentage = displayPercentage()
        if percentage >= 100 or trainStatus():
            self.timer.stop()
            self.results = QLabel("Finished Training Model")
            return
        QApplication.processEvents()
        self.pbar.setValue(int(percentage))

    def doAction(self):
        
        if self.timer.isActive():
            self.timer.stop()
            # self.btn.setText('Start')
        else:
            self.timer.start(10, self)
            # self.btn.setText('Stop')

'''
# Step 1: Create a worker class
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        for i in range(5):
            sleep(1)
            self.progress.emit(i + 1)
        self.finished.emit()

class Window(QMainWindow):
    # Snip...
    def runLongTask(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.longRunningBtn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.longRunningBtn.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
        )
        '''







    