# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys,os
import socket
from threading import Thread
from SocketServer import ThreadingMixIn
from _socket import gethostname
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Send(QtGui.QMainWindow):
    name=""
    def __init__(self):    
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(623, 549)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 240, 161, 51))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 132, 110);\n"
"font: 12pt \"Narkisim\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 601, 451))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd()+"/filesharing.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 281, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 10, 141, 41))
        self.pushButton_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(99, 182, 255);\n"
"font: 12pt \"Narkisim\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Send", None))
        self.pushButton_2.setText(_translate("MainWindow", "Select File", None))
        self.pushButton_2.clicked.connect(self.openFileDialog)
        self.pushButton.clicked.connect(self.sendFile)
        
    def openFileDialog(self):
        self.name = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        self.lineEdit.setText(self.name)
        #self.fileName,self.extension=os.path.splitext(self.name)
        self.extension = str(self.name)[str(self.name).rfind('.'):]
        print self.extension
        
    def sendFile(self):
        #self.label_2.setText('server created') 
        print self.name 
        s = socket.socket()         # Create a socket object
        host = socket.gethostname() # Get local machine name
        port = 10000                 # Reserve a port for your service.
        s.bind((host, port))
        
        print "connection created" 
              # Bind to the port
        s.listen(5)
        #while True:
        c,addr=s.accept()
        print 'got connection from',addr
        c.send(self.extension)
        #self.lineEdit_2.setText("got connection")    
        print 'sending'
        f=open(self.name,'rb')
        l=f.read(1024);
        c.send(l)
        while(l):
            l=f.read(1024)
            c.send(l)
            print 'sending...'
                
        f.close()
        print 'done sending'
        #c.send("server is closed");
        #c.send('thank you for connecting syncronisation is done')
        c.close()
        #yself.label_3.setText('server is closed click on send to create server again')


