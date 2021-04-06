import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QGridLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Handwriting Analysis')

        #grid
        grid = QGridLayout()

        #self.move(300, 300)
        #self.resize(600, 400) 
        self.setLayout(grid)       
        self.setGeometry(300, 300, 480, 320)
        self.show()

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


    #When 'Train Model' is clicked
    def showTrainWindow(self, checked):
        if self.w is None:
            self.w = trainModelWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None

class trainModelWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Handwriting Training')
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MainWindow()
   sys.exit(app.exec_())