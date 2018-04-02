# -*- coding: utf-8 -*-
import sys
import os
from PyQt4 import QtCore, QtGui

os.environ["PYTHONPATH"] = "C:/Users/ASUSarturo/Deroduction_ProjectGenerator"

import GP_UI.GP_Main_v02
reload(GP_UI.GP_Main_v02)
from GP_UI.GP_Main_v02 import Ui_MainWindow


import GP_Core.GP_Bridge
reload(GP_Core.GP_Bridge)
from GP_Core.GP_Bridge import GP_Bridge


class MyApplication(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApplication()
    window.setWindowFlags(
        window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    interfaceMacho = GP_Bridge(window=window)
    window.show()

    try:
        sys.exit(app.exec_())
    except:
        "error al intentar salir"





