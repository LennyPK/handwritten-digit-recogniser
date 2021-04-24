import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CanvasModel(QLabel):
    canvas = None
    last_x = None
    last_y = None

    def __init__(self):
        super().__init__()
        self.setupUI()
        
    def setupUI(self):
        

        self.canvas = QPixmap(600,600)
        self.painter = QPainter(self.canvas)

        self.pen = QPen(Qt.black)
        self.pen.setWidth(10)
        
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

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.canvas)
        painter.end()

    def clearCanvas(self):
        self.canvas.fill(Qt.white)
        self.update()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widg = QWidget()
    hbox = QHBoxLayout()
    label = canvasModel()
    hbox.addWidget(label)
    widg.setLayout(hbox)
    widg.show()
    sys.exit(app.exec_())



        
# self.label = QtWidgets.QLabel()
    #     self.canvas = QtGui.QPixmap(600, 600)
    #     self.canvas.fill(QtGui.QColor('#ffffff')) # Fill entire canvas white.
    #     self.label.setPixmap(self.canvas)
    #     self.grid.addWidget(self.label, 0, 0, Qt.AlignLeft)
        
    #     self.last_x, self.last_y = None, None

    # '''Drawing on the Canvas'''
    # def mouseMoveEvent(self, e):
    #     if self.last_x is None: # First event.
    #         self.last_x = e.x()
    #         self.last_y = e.y()
    #         return # Ignore the first time.

    #     painter = QtGui.QPainter(self.label.pixmap())
    #     pen = QPen(Qt.black)
    #     pen.setWidth(10)
    #     painter.setPen(pen)
    #     painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
    #     painter.end()
    #     self.update()

    #     # Update the origin for next time.
    #     self.last_x = e.x()
    #     self.last_y = e.y()

    # def mouseReleaseEvent(self, e):
    #     self.last_x = None
    #     self.last_y = None

    # def paintEvent(self, e):
    #     painter = QPainter(self)
    #     painter.drawPixmap(self.rect(), self.canvas)
    #     painter.end()

    # '''NOT WORKING'''
    # def clearCanvas(self):
    #     # print("henlo")
    #     self.canvas.fill(Qt.white)
    #     # self.label.update()
    #     # painter = QtGui.QPainter(self.label.pixmap())
    #     # pen = QtGui.QPen()
    #     # pen.setWidth(3)
    #     # pen.setColor(QtGui.QColor("#ffffff"))
    #     # painter.setPen(pen)

    #     # brush = QtGui.QBrush()
    #     # brush.setColor(QtGui.QColor("#ffffff"))
    #     # brush.setStyle(Qt.Dense1Pattern)
    #     # painter.setBrush(brush)
    #     # painter.fillRect(0, 0, 600, 600)
    #     # painter.end()
    #     # self.update()
