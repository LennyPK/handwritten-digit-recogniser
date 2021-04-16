from train_gui import*
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

class HomeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self, parent=None):

        
        # centering the window
        WinInfo = self.frameGeometry()
        MonitorInfo = QDesktopWidget().availableGeometry().center()
        WinInfo.moveCenter(MonitorInfo)
        self.move(WinInfo.topLeft())

    #When 'Train Model' is clicked
    def showTrainWindow(self, checked):
        if self.w is None:
            self.w = trainModelWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None    

class ModelUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self, parent=None):

        #setting up the size of the window
        grid = QGridLayout()
        self.setLayout(grid)

        # centering the window
        WinInfo = self.frameGeometry()
        MonitorInfo = QDesktopWidget().availableGeometry().center()
        WinInfo.moveCenter(MonitorInfo)
        self.move(WinInfo.topLeft())

        #Make buttons
        #modelBtns = QVBoxLayout()
        clearBtn = QPushButton(" &Clear")
        ranBtn = QPushButton(" &Random")
        modBtn = QPushButton(" &Model")
        recBtn = QPushButton(" &Recognise")
        grid.addWidget(clearBtn,0,1)
        grid.addWidget(ranBtn,1,1)
        grid.addWidget(modBtn,2,1)
        grid.addWidget(recBtn,3,1)

        #self.label = QLabel('hi')
        #canvas = QtGui.QPixmap(400,300)
        #self.label.setPixmap(canvas)
        #grid.addWidget(self.label,0,0,0,0)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()
        self.w = None

        #grid
        grid = QGridLayout()
        self.setLayout(grid)       
        self.setGeometry(300, 300, 1000, 800)

        #Actions
        trainAction = QAction('Train Model', self)
        #trainAction.setShortcut()
        trainAction.setStatusTip('Train Model')
        trainAction.triggered.connect(self.showTrainWindow)

        quitAction = QAction('Exit', self)
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Quit application')
        quitAction.triggered.connect(qApp.quit)

        viewTrainAction = QAction('View Training Images', self)
        #viewTrainAction.setShortcut()
        viewTrainAction.triggered.connect(self.startModelUI)


        viewTestAction = QAction('View Testing Images', self)
        #viewTestAction.setShortcut()
        #viewTestAction.setStatusTip()
        #viewTestAction.triggered.connect()

        menubar = self.menuBar()
        #File menubar (train model, quit)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(trainAction)
        filemenu.addAction(quitAction)
        viewmenu = menubar.addMenu('&View')
        viewmenu.addAction(viewTrainAction)        
        viewmenu.addAction(viewTestAction)

        self.startHomeUI()

    def startHomeUI(self):
        self.Home = HomeUI()
        self.setWindowTitle("Home")
        self.setCentralWidget(self.Home)
        self.show()

    def startModelUI(self):
        self.Model = ModelUI()
        self.setWindowTitle("Modelling Handwriting Analysis")
        self.setCentralWidget(self.Model)
        self.show()

    #When 'Train Model' is clicked
    def showTrainWindow(self, checked):
        if self.w is None:
            self.w = trainModelWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MainWindow()
   sys.exit(app.exec_())