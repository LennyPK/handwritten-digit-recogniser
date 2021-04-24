from train_gui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QTimer
from canvasFile import CanvasModel
from ReLuTrainer import *
#from sklearn_trainer import * 

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

        self.label = CanvasModel()
        self.label.setFixedSize(QSize(600, 600))
        self.grid.addWidget(self.label, 0,0)
        self.grid.addWidget(self.btnGroup(), 0,1)

        clearBtn = QPushButton(" &Clear")
        clearBtn.clicked.connect(self.label.clearCanvas)
        self.grid.addWidget(self.finalGroup(), 1, 1)
        self.grid.addWidget(self.label,0,1)
        self.setLayout(self.grid)

        '''centering the window'''
        WinInfo = self.frameGeometry()
        MonitorInfo = QDesktopWidget().availableGeometry().center()
        WinInfo.moveCenter(MonitorInfo)
        self.move(WinInfo.topLeft())

        
    def btnGroup(self):
        groupBox = QGroupBox('Buttons Group')
        
        # Make buttons
        clearBtn = QPushButton(" &Clear")
        clearBtn.clicked.connect(self.label.clearCanvas)

        ranBtn = QPushButton(" &Random")
        modBtn = QPushButton(" &Model")
        recBtn = QPushButton(" &Recognise")
        recBtn.clicked.connect(self.save_image)

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
        
    #when recognise btn pressed, save image first        
    def save_image(self):
        self.label.save_canvas()
        make_predictions()

'''ImageUI is the window to display the test images'''
class ImageUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self, parent=None):
        self.grid = QGridLayout()
        self.imageLabel = QLabel()
        self.test_image = QPixmap('img_9.png')
        self.imageLabel.setPixmap(self.test_image)
        self.grid.addWidget(self.imageLabel, 0, 0)
        self.setLayout(self.grid) 


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()
        self.trainWin = None

        self.setWindowIcon(QIcon('img_9.png'))

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

        openAnalyserAction = QAction('Open Analyser', self)
        openAnalyserAction.triggered.connect(self.startModelUI)

        viewTestAction = QAction('View Testing Images', self)
        viewTestAction.triggered.connect(self.startImageUI)

        menubar = self.menuBar()
        '''File menubar (train model, quit)'''
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(trainAction)
        filemenu.addAction(quitAction)
        '''View menubar (open analyser, view testing images)'''
        viewmenu = menubar.addMenu('&View')
        viewmenu.addAction(openAnalyserAction)        
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
        

    def startImageUI(self):
        self.Image = ImageUI()
        self.setWindowTitle("Testing Images")
        self.setCentralWidget(self.Image)
        self.show()

    #When 'Train Model' is clicked
    def showTrainWindow(self, checked):
        if self.trainWin is None:
            self.trainWin = trainModelWindow()
            self.trainWin.show()
        else:
            self.trainWin.close()
            self.trainWin = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())