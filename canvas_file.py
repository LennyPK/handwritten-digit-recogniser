import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Canvas_Model(QLabel):
    canvas = None
    last_x = None
    last_y = None

    def __init__(self):
        super().__init__()
        self.setup_UI()
        
    '''initialising QPixmap'''
    def setup_UI(self):
        
        self.canvas = QPixmap(600,600)
        self.painter = QPainter(self.canvas)

        self.pen = QPen(Qt.black)
        self.pen.setWidth(35)
        
        self.painter.setPen(self.pen)

        self.canvas.fill(QColor('#ffffff'))
        self.setPixmap(self.canvas)
        self.setAutoFillBackground(True)
        
    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        self.painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        self.setPixmap(self.canvas)
        self.update()

        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None
        # self.painter.end()
        '''uncomment if you do not want application to crash'''
        '''but in this case the Analyser needs to be refreshed'''
        
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.canvas)
        painter.end()

    '''created a function to clear the canvas'''
    def clear_canvas(self):
        self.canvas.fill(Qt.white)
        self.update()
        
    def save_canvas(self):
        self.canvas.save('saved_canvas.png')