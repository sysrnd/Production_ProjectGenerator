# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\RnD\Pipeline\Production\Production_ProjectGenerator\GP_UI\Resources\GP_Main_v03.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(513, 423)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_title = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.verticalLayout.addWidget(self.lbl_title)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.lyt_horizontal_type = QtGui.QFrame(self.centralwidget)
        self.lyt_horizontal_type.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lyt_horizontal_type.setFrameShadow(QtGui.QFrame.Raised)
        self.lyt_horizontal_type.setObjectName(_fromUtf8("lyt_horizontal_type"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.lyt_horizontal_type)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lbl_type = QtGui.QLabel(self.lyt_horizontal_type)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_type.setFont(font)
        self.lbl_type.setObjectName(_fromUtf8("lbl_type"))
        self.horizontalLayout.addWidget(self.lbl_type)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cmB_type = QtGui.QComboBox(self.lyt_horizontal_type)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmB_type.sizePolicy().hasHeightForWidth())
        self.cmB_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmB_type.setFont(font)
        self.cmB_type.setMaxVisibleItems(10)
        self.cmB_type.setObjectName(_fromUtf8("cmB_type"))
        self.cmB_type.addItem(_fromUtf8(""))
        self.cmB_type.addItem(_fromUtf8(""))
        self.cmB_type.addItem(_fromUtf8(""))
        self.cmB_type.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmB_type)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.lyt_horizontal_type)
        self.lyt_grid_dynamic = QtGui.QFrame(self.centralwidget)
        self.lyt_grid_dynamic.setMinimumSize(QtCore.QSize(0, 20))
        self.lyt_grid_dynamic.setObjectName(_fromUtf8("lyt_grid_dynamic"))
        self.gridLayout = QtGui.QGridLayout(self.lyt_grid_dynamic)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.spBx_scenes = QtGui.QSpinBox(self.lyt_grid_dynamic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spBx_scenes.sizePolicy().hasHeightForWidth())
        self.spBx_scenes.setSizePolicy(sizePolicy)
        self.spBx_scenes.setMaximumSize(QtCore.QSize(40, 16777215))
        self.spBx_scenes.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spBx_scenes.setObjectName(_fromUtf8("spBx_scenes"))

        self.gridLayout.addWidget(self.spBx_scenes, 2, 1, 1, 1)
        self.lbl_ruta = QtGui.QLabel(self.lyt_grid_dynamic)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_ruta.setFont(font)
        self.lbl_ruta.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_ruta.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lbl_ruta.setAcceptDrops(False)
        self.lbl_ruta.setObjectName(_fromUtf8("lbl_ruta"))
        self.gridLayout.addWidget(self.lbl_ruta, 0, 0, 1, 1)
        self.lbl_numScenes = QtGui.QLabel(self.lyt_grid_dynamic)
        self.lbl_numScenes.setObjectName(_fromUtf8("lbl_numScenes"))
        self.gridLayout.addWidget(self.lbl_numScenes, 2, 0, 1, 1)
        self.txt_nameProject = QtGui.QLineEdit(self.lyt_grid_dynamic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_nameProject.sizePolicy().hasHeightForWidth())
        self.txt_nameProject.setSizePolicy(sizePolicy)
        self.txt_nameProject.setMaximumSize(QtCore.QSize(120, 20))
        self.txt_nameProject.setDragEnabled(False)
        self.txt_nameProject.setObjectName(_fromUtf8("txt_nameProject"))
        self.gridLayout.addWidget(self.txt_nameProject, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.verticalLayout.addWidget(self.lyt_grid_dynamic)
        spacerItem4 = QtGui.QSpacerItem(10, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.lyt_horizontal_acceptBtns = QtGui.QFrame(self.centralwidget)
        self.lyt_horizontal_acceptBtns.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lyt_horizontal_acceptBtns.setFrameShadow(QtGui.QFrame.Raised)
        self.lyt_horizontal_acceptBtns.setObjectName(_fromUtf8("lyt_horizontal_acceptBtns"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.lyt_horizontal_acceptBtns)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.btn_aceptar = QtGui.QPushButton(self.lyt_horizontal_acceptBtns)
        self.btn_aceptar.setObjectName(_fromUtf8("btn_aceptar"))
        self.horizontalLayout_2.addWidget(self.btn_aceptar)
        self.btn_cancelar = QtGui.QPushButton(self.lyt_horizontal_acceptBtns)
        self.btn_cancelar.setObjectName(_fromUtf8("btn_cancelar"))
        self.horizontalLayout_2.addWidget(self.btn_cancelar)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout.addWidget(self.lyt_horizontal_acceptBtns)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_title.setText(_translate("MainWindow", "Project", None))
        self.lbl_type.setText(_translate("MainWindow", "Type:", None))
        self.cmB_type.setItemText(0, _translate("MainWindow", "Mexicartoon", None))
        self.cmB_type.setItemText(1, _translate("MainWindow", "Spot 2D", None))
        self.cmB_type.setItemText(2, _translate("MainWindow", "Pizarra blanca", None))
        self.cmB_type.setItemText(3, _translate("MainWindow", "Campañas", None))
        self.lbl_ruta.setText(_translate("MainWindow", "Ruta:  Z:MKF_animacion/MEXICARTOONS", None))
        self.lbl_numScenes.setText(_translate("MainWindow", "# Scenes", None))
        self.txt_nameProject.setPlaceholderText(_translate("MainWindow", "Name Project", None))
        self.btn_aceptar.setText(_translate("MainWindow", "&Accept", None))
        self.btn_cancelar.setText(_translate("MainWindow", "&Cancel", None))

