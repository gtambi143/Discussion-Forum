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
import ipAddress
from ipAddress import hostname

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

class Ui_fileSyncClient(QtGui.QMainWindow):
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
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 290, 361, 20))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 230, 101, 41))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 330, 111, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 85, 255);\n"
"font: 10pt \"Narkisim\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 240, 221, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 221, 201))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd()+"/client.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 141, 21))
        self.label_2.setStyleSheet(_fromUtf8("font: 12pt \"Narkisim\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
      
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Client Window", None))
        self.pushButton_2.setText(_translate("MainWindow", "Syncronise", None))
        self.label_2.setText(_translate("MainWindow", "Source file", None))
        self.label_3.setText('server is not ready!! click on syncronise to check that if server is ready')
        self.pushButton.setText(_translate("MainWindow", "open", None))
     
        self.pushButton.clicked.connect(self.file_open)
        self.pushButton_2.clicked.connect(self.acceptConnection)
        
            
    def file_open(self):
        #name = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.name = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        self.lineEdit.setText(self.name)
        
        
    
    def acceptConnection(self,name):
        print self.name
        s=socket.socket()
        host=hostname#'192.168.43.163'#socket.gethostname()
        port=10000
        s.connect((host,port))
        #self.lineEdit_3.
        self.label_3.setText("server is ready")   
        f=open(self.name,'rb')
        
        l=f.read(1024)
        print l
        while(l):
            s.send(l)
            l=f.read(1024)
            print l 
        f.close()
        s.send("")
        print 'done sending'
        #l=s.recv(1024)
        #print l
        #self.lineEdit_3.textEdited(l)
        s.shutdown(socket.SHUT_WR)
        s.close()
        self.label_3.setText("server is closed!! click syncronise to check if server is available")
    def showFile(self):
        print self.name
        f=open(str(self.name),'rb')
        l=f.read(1024)
        #print l
        while(l):
            l=f.read(1024)
            #print l
        f.close()
                    

            
    

