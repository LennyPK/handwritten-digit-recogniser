import sys
from train_gui import*
from PyQt5.QtWidgets import *

class HomeUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setupUI()

    def setupUI(self, parent=None):
        #grid
        grid = QGridLayout()

        self.setLayout(grid)       
        self.setGeometry(300, 300, 1000, 800)
        self.show()

        # centering the window
        WinInfo = self.frameGeometry()
        MonitorInfo = QDesktopWidget().availableGeometry().center()
        WinInfo.moveCenter(MonitorInfo)
        self.move(WinInfo.topLeft())

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

        viewTestAction = QAction('View Testing Images', self)

        menubar = self.menuBar()
        #File menubar (train model, quit)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(trainAction)
        filemenu.addAction(quitAction)

        viewmenu = menubar.addMenu('&View')
        viewmenu.addAction(viewTrainAction)        
        viewmenu.addAction(viewTestAction)

    #When 'Train Model' is clicked
    def showTrainWindow(self, checked):
        if self.w is None:
            self.w = trainModelWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None    

class ModelUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setupUI()

    def setupUI(self, parent=None):

        #grid
        grid = QGridLayout()

        self.setLayout(grid)       
        self.setGeometry(300, 300, 1000, 800)
        self.show()

        # centering the window
        WinInfo = self.frameGeometry()
        MonitorInfo = QDesktopWidget().availableGeometry().center()
        WinInfo.moveCenter(MonitorInfo)
        self.move(WinInfo.topLeft())

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
        #viewTrainAction.setStatusTip()
        #viewTrainAction.triggered.connect()


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

        #Make buttons
        modelBtns = QVBoxLayout()
        clearBtn = QPushButton(" &Clear")
        ranBtn = QPushButton(" &Random")
        modBtn = QPushButton(" &Model", self)
        recBtn = QPushButton(" &Recognise", self)
        modelBtns.addWidget(clearBtn)
        modelBtns.addWidget(ranBtn)
        modelBtns.addWidget(modBtn)
        modelBtns.addWidget(recBtn)
        self.setLayout(modelBtns)

    #When 'Train Model' is clicked
    def showTrainWindow(self, checked):
        if self.w is None:
            self.w = trainModelWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None



    #When 'Train Model' is clicked
    def showTrainWindow(self, checked):
        if self.w is None:
            self.w = trainModelWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None
            
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()
        self.startHomeUI()

    def startHomeUI(self):
        self.Home = HomeUI()
        self.setWindowTitle("Home")
        self.setCentralWidget(self.Home)
        self.show()

    def startModelUI(self):
        self.Model = ModelUI(self)
        self.setWindowTitle("Modelling Handwriting Analysis")
        self.setCentralWidget(self.Model)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MainWindow()
   sys.exit(app.exec_())