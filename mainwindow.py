from PyQt4 import uic
from time import sleep
from PyQt4.QtCore import *
from PyQt4.QtGui import *

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        o = Opening(self)
        self.central_widget.addWidget(o)
        self.setGeometry(40,40,500,550)
        self.setWindowTitle( 'Minor' )
        self.show()
        
    def wind2(self):
        win2 = Win2(self)
        self.central_widget.addWidget(win2)
        self.central_widget.setCurrentWidget(win2)

    def wind3(self):
        win3 = Win3(self)
        self.central_widget.addWidget(win3)
        self.central_widget.setCurrentWidget(win3)

        
    def __del__ ( self ):
        self.ui = None

class Opening(QWidget):
    def __init__(self, parent=None):
        super(Opening, self).__init__(parent)
        label = QLabel(self)
        pixmap = QPixmap("ic.png")
        label.setPixmap(pixmap)
        label.setGeometry(30,30,400,300)
        label.move(60,30)
        lb1 = QLabel("A forum to scrum development teams \ncomes and discuss their views \non their project!!!",self)
        nfont = QFont("Times", 18, QFont.Bold)
        lb1.setFont(nfont)
        lb1.move(50,350)
        but1 = QPushButton("Continue",self)
        but1.move(200,450)
        but1.clicked.connect(self.parent().wind2)
        

class Win2(QWidget):
    def __init__(self, parent=None):
        super(Win2, self).__init__(parent)
        lb1 = QLabel("\tWelcome !!!! \nChoose any of the below to procede",self)
        nfont = QFont("Times", 18, QFont.Bold)
        lb1.setFont(nfont)
        lb1.move(50,40)
        
        but1 = QPushButton("Create a new Game",self)
        but1.move(50,130)
        but1.clicked.connect(self.parent().wind3)
        
        but2 = QPushButton("View saved Games",self)
        but2.move(50,180)
        #but2.clicked.connect(self.parent().wind2)
        
        but3 = QPushButton("    Chat with the   \nScrum Master",self)
        but3.move(50,230)
        #but3.clicked.connect(self.parent().wind2)
        
        but4 = QPushButton("     Open your    \nshared drives",self)
        but4.move(50,280)
        #but4.clicked.connect(self.parent().wind2)
        
        but5 = QPushButton("Exit",self)
        but5.move(50,330)
        but5.clicked.connect(QCoreApplication.quit)
        
        self.parent().setGeometry(40,40,500,450)
        
        
class Win3(QWidget):
    def __init__(self, parent=None):
        super(Win3, self).__init__(parent)
        lb1 = QLabel("\tCreate the Game",self)
        nfont = QFont("Cursive", 14, QFont.Bold)
        lb1.setFont(nfont)
        lb1.move(50,40)
        
        lb2 = QLabel("Name:",self)
        nfnt = QFont("Times", 10,QFont.StyleItalic)
        lb2.setFont(nfnt)
        lb2.move(50,85)
        logOutput = QTextEdit(self)
        logOutput.setGeometry(10,10,400,30)
        logOutput.move(50,100)
        
        lb3 = QLabel("Description:",self)
        lb3.setFont(nfnt)
        lb3.move(50,150)
        tA1 = QTextEdit(self)
        tA1.setGeometry(10,10,400,50)
        tA1.move(50,165)
        