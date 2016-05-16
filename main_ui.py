# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from syncAsk_ui import *
from askFile import *
from askChat import *
import os,sys

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
    
class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        #self.central_widget = QtGui.QStackedWidget()
        #self.setCentralWidget(self.central_widget)
       
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(647, 484)
        MainWindow.setStyleSheet(_fromUtf8("background-color:white\n"""))
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 400, 121, 41))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 75, 30);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 10pt \"Narkisim\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 350, 121, 41))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 10pt \"Narkisim\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(374, 400, 121, 41))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 127);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 10pt \"Narkisim\";"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(374, 350, 121, 41))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 10pt \"Narkisim\";"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 391, 241))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd()+"/discussion-forum.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 0, 231, 81))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd()+"/disussion.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "File Syncronisation", None))
        self.pushButton_2.setText(_translate("MainWindow", "Chat with users", None))
        self.pushButton_3.setText(_translate("MainWindow", "Start a Story", None))
        self.pushButton_4.setText(_translate("MainWindow", "File sharing", None))
        self.pushButton.clicked.connect(self.handleSyncButton)
        self.pushButton_4.clicked.connect(self.handleFileButton)
        self.pushButton_2.clicked.connect(self.handlePrivateChat)
        self.pushButton_3.clicked.connect(self.handleStartStory)

    def handleSyncButton(self):
        self.window = QtGui.QMainWindow()
        self.ui=Ui_syncAsk()
        self.ui.setupUi(self.window)
        self.window.show()        
    def handleFileButton(self):
        self.window=QtGui.QMainWindow()
        self.ui=Ui_askFile()
        self.ui.setupUi(self.window)
        self.window.show()
    def handlePrivateChat(self):
        self.window=QtGui.QMainWindow()
        self.ui=Ui_askChat()
        self.ui.setupUi(self.window)
        self.window.show()
    def handleStartStory(self):
        prev=os.getcwd()
        os.chdir("C:\Program Files (x86)\Google\google_appengine\launcher")
        os.system("GoogleAppEngineLauncher.exe")
        os.chdir(prev)
       
