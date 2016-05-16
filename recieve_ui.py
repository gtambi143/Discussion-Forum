# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recieve.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys,os
import socket
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

class Ui_Recieve(QtGui.QMainWindow):
    def __init__(self):    
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(687, 557)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 601, 451))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd()+"/filesharing.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100,20,500, 20))
        self.label_3.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 230, 161, 51))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 132, 110);\n"
"font: 12pt \"Narkisim\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270,20, 151, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 0, 121, 16))
        self.label_2.setStyleSheet(_fromUtf8("font: 10pt \"Narkisim\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Recieve", None))
        self.label_3.setText('give name to the new file')
        self.pushButton.clicked.connect(self.fileRecieve)
    
    def fileRecieve(self):
        s=socket.socket()
        host='192.168.43.163'#socket.gethostname()
        port=10000
        s.connect((host,port))
        #self.lineEdit_3.
        #self.label_3.setText("server is ready")
        x=self.lineEdit.text()
        ext=s.recv(1024)  
        print (x+ext) 
        f=open(x+ext,'wb')
        l=s.recv(1024)
        f.write(l)
        while(l):
            l=s.recv(1024)
            f.write(l)
        
        f.close()    
        #l=s.recv(1024)
        #print l
        #self.lineEdit_3.textEdited(l)
        
        s.close()
        #self.label_3.setText("server is closed!! click syncronise to check if server is available")
  
                   

