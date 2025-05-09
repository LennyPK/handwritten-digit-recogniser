import sys
from main_window import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ReLu_trainer import *
from worker_thread import *

'''This window is for when File -> Train is clicked'''
class Train_Model_Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()
        '''setting up threadpool'''
        self.threadpool = QThreadPool()
        self.model_number = 0

    def init_UI(self):

        self.setWindowTitle('Model Training')
        self.setWindowIcon(QIcon('scripts/logo.png'))

        self.show()
        
        self.message = QLabel("Select a Model to start training")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setFont(QFont('Cambria', 20))

        '''accuracy display'''
        self.accuracy_label = QLabel(f'Accuracy\n{get_accuracy():.0f}%')
        self.accuracy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.accuracy_label.setFont(QFont('Cambria', 15))

        '''initialising progress bar'''
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,500,25)
        self.pbar.setValue(0)
        
        self.timer = QBasicTimer()

        self.pbar.show() 

        grid_layout = QtWidgets.QGridLayout()
        grid_layout.addWidget(self.message, 0, 0)
        grid_layout.addWidget(self.button_group(), 1, 0)
        grid_layout.addWidget(self.accuracy_label, 2, 0)
        grid_layout.addWidget(self.pbar, 3, 0)

        self.setLayout(grid_layout)

    '''buttons to select different "models" to be trained'''
    def button_group(self):
        group_box = QGroupBox('Models')
        
        self.train_button_1 = QPushButton('&Model 1 (5 Epochs)\nLow Accuracy',self)
        self.train_button_1.clicked.connect(self.do_action)
        self.train_button_1.clicked.connect(self.model_1_thread)
        self.train_button_1.clicked.connect(self.disable_buttons)
        self.train_button_1.show()

        self.train_button_2 = QPushButton('&Model 2 (10 Epochs)\nHigher Accuracy',self)
        self.train_button_2.clicked.connect(self.do_action)
        self.train_button_2.clicked.connect(self.model_2_thread)
        self.train_button_2.clicked.connect(self.disable_buttons)
        self.train_button_2.show()

        self.train_button_3 = QPushButton('&Model 1 (15 Epochs)\nRecommended',self)
        self.train_button_3.clicked.connect(self.do_action)
        self.train_button_3.clicked.connect(self.model_3_thread)
        self.train_button_3.clicked.connect(self.disable_buttons)
        self.train_button_3.show()

        self.train_button_4 = QPushButton('&Model 1 (20 Epochs)\nHighest Accuracy',self)
        self.train_button_4.clicked.connect(self.do_action)
        self.train_button_4.clicked.connect(self.model_4_thread)
        self.train_button_4.clicked.connect(self.disable_buttons)
        self.train_button_4.show()

        buttn_box = QHBoxLayout()
        buttn_box.addWidget(self.train_button_1)
        buttn_box.addWidget(self.train_button_2)
        buttn_box.addWidget(self.train_button_3)
        buttn_box.addWidget(self.train_button_4)

        group_box.setLayout(buttn_box)

        return group_box

    '''timer to update progress bar'''
    def timerEvent(self, e):
        percentage = display_percentage()

        '''checks if training is finished and updates progress bar to 100%'''
        if percentage >= 100  or train_status():
            self.timer.stop()
            self.message.setText(f"Finished Training Model {self.get_model_number()}")
            self.pbar.setValue(100)

            '''printing accuracy'''
            self.accuracy_label.setText(f'Accuracy\n{get_accuracy():.0f}%')

            self.enable_buttons()

            return
        '''updates progress bar as training progresses'''
        self.pbar.setValue(int(percentage))

        '''printing accuracy'''
        self.accuracy_label.setText(f'Accuracy\n{get_accuracy():.0f}%')

    '''timer for progress bar'''
    def do_action(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(10, self)
    
    '''multithreaded functions'''
    def model_1_thread(self):
        worker = Worker_1()
        self.threadpool.start(worker)
        self.model_number = 1

    def model_2_thread(self):
        worker = Worker_2()
        self.threadpool.start(worker)
        self.model_number = 2

    def model_3_thread(self):
        worker = Worker_3()
        self.threadpool.start(worker)
        self.model_number = 3

    def model_4_thread(self):
        worker = Worker_4()
        self.threadpool.start(worker)
        self.model_number = 4

    def get_model_number(self):
        return self.model_number

    def disable_buttons(self):
        self.train_button_1.setEnabled(False)
        self.train_button_2.setEnabled(False)
        self.train_button_3.setEnabled(False)
        self.train_button_4.setEnabled(False)

    def enable_buttons(self):
        self.train_button_1.setEnabled(True)
        self.train_button_2.setEnabled(True)
        self.train_button_3.setEnabled(True)
        self.train_button_4.setEnabled(True)
