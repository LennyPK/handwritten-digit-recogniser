import sys
from train_gui import*
from PyQt5.QtWidgets import *


class ModelMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Handwriting Analysis')

        #grid
        grid = QGridLayout()
        self.setLayout(grid)     

        grid.addWidget(Q)


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



