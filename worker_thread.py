'''
M. Fitzpatrick, "Multithreading PyQt applications with QThreadPool", LearnPyQt, April 15, 2017. Accessed on April 18, 2021. [Online]. Availble:
https://www.mfitzp.com/tutorials/multithreading-pyqt-applications-qthreadpool/
'''

from PyQt5.QtCore import *
from ReLu_trainer import *

'''making other threads, for different epochs, different "models" '''
class Worker_1(QRunnable):

    @pyqtSlot()
    def run(self):
        test_input(1, 5)

class Worker_2(QRunnable):

    @pyqtSlot()
    def run(self):
        test_input(1, 10)

class Worker_3(QRunnable):

    @pyqtSlot()
    def run(self):
        test_input(1, 15)

class Worker_4(QRunnable):

    @pyqtSlot()
    def run(self):
        test_input(1, 20)


