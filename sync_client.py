from PyQt4 import QtCore, QtGui
from pysync_client_ui import *
import sys
if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    ex= Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
