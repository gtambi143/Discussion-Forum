# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'syncAsk.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from send_ui import *
from recieve_ui import *
from pysync_client_ui import *
import sys,os
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

class Ui_askFile(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(636, 491)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 501, 201))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd()+"/filesharing1.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 260, 161, 51))
        self.label_2.setStyleSheet(_fromUtf8("font: 75 16pt \"Narkisim\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 360, 111, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 360, 111, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 127);\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 380, 21, 16))
        self.label_3.setStyleSheet(_fromUtf8("font: 14pt \"Narkisim\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Who are you ?", None))
        self.pushButton.setText(_translate("MainWindow", "Server", None))
        self.pushButton_2.setText(_translate("MainWindow", "Client", None))
        self.label_3.setText(_translate("MainWindow", "or", None))
        
        self.pushButton.clicked.connect(self.openSend)
        self.pushButton_2.clicked.connect(self.openRecieve)
    
    def openSend(self):
        self.window = QtGui.QMainWindow()
        self.ui=Ui_Send()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openRecieve(self):
        self.window = QtGui.QMainWindow()
        self.ui=Ui_Recieve()
        self.ui.setupUi(self.window)
        self.window.show() 
