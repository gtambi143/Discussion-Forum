from PyQt4 import QtCore, QtGui
from send_ui import *
import sys
import socket
import time
if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    ex= Ui_Send()
    ex.show()
        
    sys.exit(app.exec_())