import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Handwriting Analysis')
        self.move(300, 300)
        self.resize(600, 400)        
        self.show()


        #exitAction = QAction(QIcon('D:\workspace\COMPSYS302_PyQt5\exit.png'), 'Exit', self)
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Quit application')
        quitAction.triggered.connect(qApp.quit)
        

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())