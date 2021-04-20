from train_gui import*
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QTimer

'''HomeUI is the window that shows up when we run the code'''
class HomeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self, parent=None):
        '''Text on the Home Window'''
        self.layout = QGridLayout()
        self.label = QLabel("Handwritten\nDigit Analyser")
        self.layout.addWidget(self.label, 0, 0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QFont('Cambria', 80))
        self.label.setWordWrap(True)
        self.setLayout(self.layout) 


'''ModelUI is the window that is used when dealing with the drawing canvas'''
class ModelUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    '''setupUI() is used to place and set up the group boxes used in ModelUI'''
    def setupUI(self, parent=None):
        self.grid = QGridLayout()

        #grid.addWidget(self.drawingCanvasGroup(), 0,0)
        self.grid.addWidget(self.btnGroup(), 0,1)
        self.grid.addWidget(self.finalGroup(), 1, 1)
        self.setLayout(self.grid)

        '''centering the window'''
        WinInfo = self.frameGeometry()
        MonitorInfo = QDesktopWidget().availableGeometry().center()
        WinInfo.moveCenter(MonitorInfo)
        self.move(WinInfo.topLeft())

        '''making the canvas and adding it the layout'''
        self.label = QtWidgets.QLabel()
        self.canvas = QtGui.QPixmap(600, 600)
        self.canvas.fill(QtGui.QColor('#ffffff')) # Fill entire canvas white.
        self.label.setPixmap(self.canvas)
        self.grid.addWidget(self.label, 0, 0, Qt.AlignLeft)
        self.last_x, self.last_y = None, None

    '''Drawing on the Canvas'''
    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        painter = QtGui.QPainter(self.label.pixmap())
        pen = QPen(Qt.black)
        pen.setWidth(10)
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

    '''NOT WORKING'''
    def clearCanvas(self):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.fillRect(0, 0, 600, 600, color='white')
        painter.end()
        self.update()

    def btnGroup(self):
            groupBox = QGroupBox('Buttons Group')
            
            # Make buttons
            clearBtn = QPushButton(" &Clear")
            clearBtn.clicked.connect(self.clearCanvas)

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

        # Actions
        trainAction = QAction('Train Model', self)
        trainAction.setShortcut('Ctrl+T')
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
        self.setWindowTitle("Handwritten Digit Recongizition")
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