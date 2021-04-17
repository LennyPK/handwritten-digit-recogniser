from train_gui import*
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


'''HomeUI is the window that shows up when we run the code'''
class HomeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self, parent=None):
        label = QLabel("Modelling Analysis")  


'''ModelUI is the window that is used when dealing with the drawing canvas'''
class ModelUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    '''setupUI() is used to place and set up the group boxes used in ModelUI'''
    def setupUI(self, parent=None):

        # setting up the layout of the window into groups
        grid = QGridLayout()


        #grid.addWidget(self.drawingCanvasGroup(), 0,0)
        grid.addWidget(self.btnGroup(), 0,1)
        grid.addWidget(self.finalGroup(), 1, 1)
        self.setLayout(grid)

        # centering the window
        WinInfo = self.frameGeometry()
        MonitorInfo = QDesktopWidget().availableGeometry().center()
        WinInfo.moveCenter(MonitorInfo)
        self.move(WinInfo.topLeft())

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(600, 600)
        canvas.fill(QtGui.QColor('#ffffff')) # Fill entire canvas white.
        self.label.setPixmap(canvas)
        grid.addWidget(self.label,0,0,Qt.AlignLeft)
        self.last_x, self.last_y = None, None

    def btnGroup(self):
            groupBox = QGroupBox('Buttons Group')
            
            # Make buttons
            clearBtn = QPushButton(" &Clear")
            ranBtn = QPushButton(" &Random")
            modBtn = QPushButton(" &Model")
            recBtn = QPushButton(" &Recognise")

            btnBox = QVBoxLayout()
            btnBox.addWidget(clearBtn)
            btnBox.addWidget(ranBtn)
            btnBox.addWidget(modBtn)
            btnBox.addWidget(recBtn)

            groupBox.setLayout(btnBox)

            return groupBox

    '''Placeholding box at the moment'''
    def finalGroup(self):
        groupBox = QGroupBox('Predictions')

        return groupBox


    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        painter = QtGui.QPainter(self.label.pixmap())
        pen = QPen(Qt.black)
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()
        self.w = None

        #grid
        grid = QGridLayout()
        self.setLayout(grid)       
        self.setGeometry(300, 300, 1000, 800)

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