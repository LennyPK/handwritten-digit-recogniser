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

        #Actions
        quitAction = QAction('Exit', self)
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Quit application')
        quitAction.triggered.connect(qApp.quit)

        trainModel = QAction('Train Model', self)
        #trainModel.setShortcut()
        trainModel.setStatusTip('Train Model')

        menubar = self.menuBar()
        #File menubar (train model, quit)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(quitAction)
        filemenu.addAction(trainModel)
        

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())