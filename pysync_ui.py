# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pysync.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys,os
import socket
import time

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

class Ui_fileSyncServer(QtGui.QMainWindow):
    name=""  
    def __init__(self):    
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600,500)
        MainWindow.setStyleSheet("background-color:white")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 321, 230))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd()+"/server.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 240, 141, 21))
        self.label_2.setStyleSheet(_fromUtf8("font: 12pt \"Narkisim\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 240, 221, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 230, 101, 41))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 330, 111, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 85, 255);\n"
"font: 10pt \"Narkisim\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 290, 361, 20))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 574, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Server Window", None))
        self.pushButton_2.setText(_translate("MainWindow", "Syncronise", None))
        self.label_2.setText(_translate("MainWindow", "select destination file", None))
        self.label_3.setText('server not created')
        self.pushButton.setText(_translate("MainWindow", "open", None))
        
        self.pushButton.clicked.connect(self.file_open)
        self.pushButton_2.clicked.connect(self.createConnection)
    
    def file_open(self):
        #name = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.name = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        
        self.lineEdit.setText(self.name)
    
    def getFileName(self):
        return self.name    
    
    def createConnection(self,name):
        
        
        print self.name 
        s = socket.socket()         # Create a socket object
        host = socket.gethostname() # Get local machine name
        port = 10000                 # Reserve a port for your service.
        s.bind((host, port))
        
        print "connection created" 
              # Bind to the port
        s.listen(5)
       
        c,addr=s.accept()
        print 'got connection from',addr
        
         
        print 'syncronising'
        f=open(self.name,'wb')
        while True:
            
            l=c.recv(1024)
            #print l
            if not l:
                break
            f.write(l)
                
        f.close()
        print 'done syncronising'
        
        c.close()
        self.label_3.setText('server is closed click on syncronise to create server again')
       
    
            
    

            
	

