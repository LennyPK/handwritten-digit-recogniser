from PyQt5.QtCore import *
from ReLuTrainer import *

'''making other threads, for different epochs, different "models"'''
class Worker_1(QRunnable):

    @pyqtSlot()
    def run(self):
        testInput(1, 5)

class Worker_2(QRunnable):

    @pyqtSlot()
    def run(self):
        testInput(1, 10)

class Worker_3(QRunnable):

    @pyqtSlot()
    def run(self):
        testInput(1, 15)

class Worker_4(QRunnable):

    @pyqtSlot()
    def run(self):
        testInput(1, 20)


