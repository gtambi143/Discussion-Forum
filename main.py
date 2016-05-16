from PyQt4 import QtCore, QtGui
from main_ui import *
import sys
import socket
import time
if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    ex= Ui_MainWindow()
    ex.show()
        
    sys.exit(app.exec_())
