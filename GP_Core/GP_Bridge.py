# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class GP_Bridge(object):

	def __init__(self, window):
		'''
		'''
		self.sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)

		self.window = window
		self.window.spBx_scenes.setMinimum(1)
		self.window.lbl_ruta.setMinimumSize(QtCore.QSize(300, 25))

		self.reg_ex = QtCore.QRegExp("[a-zA-Z0-9_]+")
		validator = QtGui.QRegExpValidator(self.reg_ex, self.window.txt_nameProject)
		self.window.txt_nameProject.setValidator(validator)
		
		QtCore.QObject.connect(self.window.cmB_type, QtCore.SIGNAL("currentIndexChanged(QString)"), self.populateUI)
		QtCore.QObject.connect(self.window.spBx_scenes, QtCore.SIGNAL("valueChanged(int)"), self.escenaUI)
		QtCore.QObject.connect(self.window.txt_nameProject, QtCore.SIGNAL("textChanged(QString)"), self.populateUI)

		self.window.btn_aceptar.clicked.connect(self.openExplorer)

		self.UIDict = {0: self.mexicartoon, 1: self.spot, 2: self.pizarra, 3: self.campana}
		self.visibleItems = []
		self.scenes = []
		self.contador = 4

		self.populateUI()

	def populateUI(self):

		functionToCall = self.UIDict[self.window.cmB_type.currentIndex()]()
		self.escenaUI()

	def escenaUI(self):
		val = self.window.spBx_scenes.value()
		####TODO query actual windows size
		self.window.resize(513, 1)

		numWidgets = 3

		if len(self.scenes) < val * numWidgets:
		#increment spinbox
			project = QtGui.QLineEdit()
			project.setPlaceholderText('Nombre Escena ' + str(val))
			project.setMaximumSize(QtCore.QSize(100, 25))

			self.window.gridLayout.addWidget(project, self.contador, 0, 1 ,1)
			
			self.scenes.append(project)
			

			self.contador += 1

			planos = QtGui.QLabel()
			planos.setText('# Planos Escena ' + str(val))
			self.window.gridLayout.addWidget(planos, self.contador, 0, 1 ,1)
			self.scenes.append(planos)
			
			spBox_planos = QtGui.QSpinBox()
			self.window.gridLayout.addWidget(spBox_planos, self.contador, 1, 1 ,1)
			spBox_planos.setMaximumSize(QtCore.QSize(40, 25))
			spBox_planos.setSizePolicy(self.sizePolicy)
			self.scenes.append(spBox_planos)

			self.contador += 1

		elif len(self.scenes) > val * numWidgets:
		#decrement spinbox
			for x in range(1, numWidgets + 1):
				self.scenes[len(self.scenes) - x].deleteLater()
			
			self.scenes = self.scenes[:-numWidgets]

			self.contador -= 1

	def mexicartoon(self):
		'''
		'''
		basePath = 'Z:/MKF_animacion/MEXICARTOONS/'
		path = self.getProjectName(basePath)

		self.window.lbl_ruta.setText(path)

		#self.destroyUIbyList()
		#self.destroyUIbyLayout()

	def spot(self):
		'''
		'''
		basePath = 'Z:/MKF_animacion 2D/'
		path = self.getProjectName(basePath)
		self.window.lbl_ruta.setText(path)
		#self.destroyUIbyList()
		#self.destroyUIbyLayout()

	def pizarra(self):
		'''
		'''
		basePath = 'Z:/MKF_pizarra blanca/'
		path = self.getProjectName(basePath)
		self.window.lbl_ruta.setText(path)
		#self.destroyUIbyList()
		#self.destroyUIbyLayout()

	def campana(self):
		basePath = 'Z:/MKF_animacion/CAMPANAS 2018/'
		path = self.getProjectName(basePath)
		self.window.lbl_ruta.setText(path)
		#self.destroyUIbyList()
		#self.destroyUIbyLayout()	

	def getProjectName(self, basePath):

		path = basePath

		pPath = self.window.txt_nameProject.text()
		if str(pPath) != '':
			path += str(self.window.txt_nameProject.text())
			path += '/'
		else:
			pass

		return path

	def destroyUIbyList(self):
		'''
		method 1 to delete UI elements by appending to a list after it's created 
		and calling it when new UI elements need to be changed
		'''

		for item in self.visibleItems:
			item.deleteLater()
			self.visibleItems.remove(item)

	def destroyUIbyLayout(self):
		'''
		method 2 where elements in a specific layout are deleted without the need to be queried previously
		'''

		for i in reversed(range(self.window.gridLayout.count())): 
			try:
				
				if str(self.window.gridLayout.itemAt(i).widget().objectName()) == '':
					widgetDelete = self.window.gridLayout.itemAt(i).widget()
					widgetDelete.deleteLater()
					#widgetDelete.setParent(None)
			except:
				if str(self.window.gridLayout.itemAt(i).spacerItem()) == '':
					itemDelete = self.window.gridLayout.itemAt(i).item()
					itemDelete.deleteLater()
					#widgetDelete.setParent(None)
				
	def openExplorer(self):

		import os
		os.startfile(str(self.window.lbl_ruta.text()))