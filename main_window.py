from train_gui import*
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QTimer
from canvas_file import *

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

        self.message = QLabel("To Use Painter Simultaneously, Relaunch Analyser by going to Home")
        self.grid.addWidget(self.message, 1, 0)

        '''adding canvas'''
        self.label = Canvas_Model()
        self.label.setFixedSize(QSize(600, 600))
        self.grid.addWidget(self.label, 0,0)

        self.grid.addWidget(self.button_group(), 0,1)

        '''connecting buttons'''
        clear_button = QPushButton(" &Clear")
        clear_button.clicked.connect(self.label.clear_canvas)

        self.grid.addWidget(self.final_group(), 1, 1)
        self.grid.addWidget(self.label,0,1)
        self.setLayout(self.grid)

    '''buttons for operating the canvas'''
    def button_group(self):
        group_box = QGroupBox('Buttons Group')
        
        clear_button = QPushButton(" &Clear")
        clear_button.clicked.connect(self.label.clear_canvas)

        random_button = QPushButton(" &Random")

        recognise_button = QPushButton(" &Recognise")
        recognise_button.clicked.connect(self.save_image)


        button_box = QVBoxLayout()
        button_box.addWidget(clear_button)
        button_box.addWidget(random_button)
        button_box.addWidget(recognise_button)

        group_box.setLayout(button_box)

        return group_box

    '''Placeholding box at the moment'''
    def final_group(self):
        group_box = QGroupBox('Predictions')

        return group_box   

    '''when recognise btn pressed, save image first'''
    def save_image(self):
        self.label.save_canvas()
        make_predictions()     

'''Image_UI is the window to display the test images'''
class Image_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_UI()

    def setup_UI(self, parent=None):
        self.grid = QGridLayout()
        self.grid.addWidget(self.image_set(), 0, 0)        
        self.setLayout(self.grid) 
    
    '''placeholder images'''
    def image_set(self,parent = None):
        group_box = QGroupBox('Images')

        self.image_label1 = QLabel()
        self.test_image = QPixmap('MNIST_img.png')
        self.image_label1.setPixmap(self.test_image)

        self.image_label2 = QLabel()
        self.image_label2.setPixmap(self.test_image)

        self.image_label3 = QLabel()
        self.image_label3.setPixmap(self.test_image)

        self.image_label4 = QLabel()
        self.image_label4.setPixmap(self.test_image)

        self.image_label5 = QLabel()
        self.image_label5.setPixmap(self.test_image)

        self.image_label6 = QLabel()
        self.image_label6.setPixmap(self.test_image)

        self.image_label7 = QLabel()
        self.image_label7.setPixmap(self.test_image)

        self.image_label8 = QLabel()
        self.image_label8.setPixmap(self.test_image)

        self.image_label9 = QLabel()
        self.image_label9.setPixmap(self.test_image)

        self.grid = QGridLayout()
        self.grid.addWidget(self.image_label1, 0, 0)
        self.grid.addWidget(self.image_label2, 0, 1)
        self.grid.addWidget(self.image_label3, 0, 2)
        self.grid.addWidget(self.image_label4, 1, 0)
        self.grid.addWidget(self.image_label5, 1, 1)
        self.grid.addWidget(self.image_label6, 1, 2)
        self.grid.addWidget(self.image_label7, 2, 0)
        self.grid.addWidget(self.image_label8, 2, 1)
        self.grid.addWidget(self.image_label9, 2, 2)

        group_box.setLayout(self.grid)
        return group_box


class Main_Window(QMainWindow):
    def __init__(self, parent=None):
        super(Main_Window,self).__init__()
        self.train_win = None

        self.setWindowIcon(QIcon('logo.png'))

        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(300, 300, 1000, 800)

        '''centering the window'''
        win_info = self.frameGeometry()
        monitor_info = QDesktopWidget().availableGeometry().center()
        win_info.moveCenter(monitor_info)
        self.move(win_info.topLeft())

        '''Drop-down menus'''
        home_action = QAction('Home',self)
        home_action.setShortcut('Ctrl+1')
        home_action.triggered.connect(self.start_Home_UI)

        train_action = QAction('Train Model', self)
        train_action.setShortcut('Ctrl+T')
        train_action.triggered.connect(self.show_train_window)

        quit_action = QAction('Exit', self)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.triggered.connect(qApp.quit)

        open_analyser_action = QAction('Open Analyser', self)
        open_analyser_action.triggered.connect(self.start_Module_UI)

        view_test_action = QAction('View Testing Images', self)
        view_test_action.triggered.connect(self.start_Image_UI)

        menu_bar = self.menuBar()
        '''File menu_bar (train model, quit)'''
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(home_action)
        file_menu.addAction(train_action)
        file_menu.addAction(quit_action)
        '''View menu_bar (open analyser, view testing images)'''
        view_menu = menu_bar.addMenu('&View')
        view_menu.addAction(open_analyser_action)        
        view_menu.addAction(view_test_action)

        self.start_Home_UI()

    def start_Home_UI(self):
        self.Home = Home_UI()
        self.setWindowTitle("Handwritten Digit Recognition")
        self.setCentralWidget(self.Home)
        self.show()

    def start_Module_UI(self):
        self.Model = Model_UI()
        self.setWindowTitle("Modelling Handwriting Analysis")
        self.setCentralWidget(self.Model)
        self.show()
        

    def start_Image_UI(self):
        self.Image = Image_UI()
        self.setWindowTitle("Testing Images")
        self.setCentralWidget(self.Image)
        self.show()

    '''when train model is clicked'''
    def show_train_window(self, checked):
        if self.train_win is None:
            self.train_win = Train_Model_Window()
            self.train_win.show()
        else:
            self.train_win.close()
            self.train_win = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    sys.exit(app.exec_())