from train_gui import*
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QTimer
from canvasFile import *

'''Home_UI is the window that shows up when we run the code'''
class Home_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_UI()

    def setup_UI(self, parent=None):
        '''Text on the Home Window'''
        self.layout = QGridLayout()
        self.label = QLabel("Handwritten\nDigit Analyser")
        self.layout.addWidget(self.label, 0, 0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QFont('Cambria', 80))
        self.label.setWordWrap(True)
        self.setLayout(self.layout)


'''Model_UI is the window that is used when dealing with the drawing canvas'''
class Model_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_UI()

    '''setup_UI() is used to place and set up the group boxes used in Model_UI'''
    def setup_UI(self, parent=None):

        self.grid = QGridLayout()

        self.message = QLabel("To Use Painter Simultaneously, Relaunch Analyser")
        self.grid.addWidget(self.message, 1, 0)

        self.label = Canvas_Model()
        self.label.setFixedSize(QSize(600, 600))
        self.grid.addWidget(self.label, 0,0)

        self.grid.addWidget(self.button_group(), 0,1)

        clear_button = QPushButton(" &Clear")
        clear_button.clicked.connect(self.label.clear_canvas)

        self.grid.addWidget(self.finalGroup(), 1, 1)
        self.grid.addWidget(self.label,0,1)
        self.setLayout(self.grid)

        '''centering the window'''
        WinInfo = self.frameGeometry()
        MonitorInfo = QDesktopWidget().availableGeometry().center()
        WinInfo.moveCenter(MonitorInfo)
        self.move(WinInfo.topLeft())

        
    def button_group(self):
        groupBox = QGroupBox('Buttons Group')
        
        # Make buttons
        clear_button = QPushButton(" &Clear")
        clear_button.clicked.connect(self.label.clear_canvas)

        random_button = QPushButton(" &Random")
        model_button = QPushButton(" &Model")
        recognise_button = QPushButton(" &Recognise")

        btnBox = QVBoxLayout()
        btnBox.addWidget(clear_button)
        btnBox.addWidget(random_button)
        btnBox.addWidget(model_button)
        btnBox.addWidget(recognise_button)

        groupBox.setLayout(btnBox)

        return groupBox

    '''Placeholding box at the moment'''
    def finalGroup(self):
        groupBox = QGroupBox('Predictions')

        return groupBox        

'''ImageUI is the window to display the test images'''
class ImageUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_UI()

    def setup_UI(self, parent=None):
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
        self.Home = Home_UI()
        self.setWindowTitle("Handwritten Digit Recongizition")
        self.setCentralWidget(self.Home)
        self.show()

    def startModelUI(self):
        self.Model = Model_UI()
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