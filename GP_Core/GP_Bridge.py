# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class GP_Bridge(object):
	def __init__(self, window):
		'''
		'''

		self.window = window
		QtCore.QObject.connect(self.window.cmB_type, QtCore.SIGNAL("currentIndexChanged(QString)"), self.populateUI)
		
		self.UIDict = {0: self.mexicartoon, 1: self.spot, 2: self.marca, 3: self.campana}
		self.visibleItems = []

		self.populateUI()

	def populateUI(self):

		functionToCall = self.UIDict[self.window.cmB_type.currentIndex()]()
		

	def mexicartoon(self):
		'''
		'''
		#self.destroyUIbyList()
		self.destroyUIbyLayout()

		spinBox = QtGui.QSpinBox()
		self.window.gridLayout.addWidget(spinBox, 0, 0, 1, 1)
		self.visibleItems.append(spinBox)

		spacer = QtGui.QSpacerItem(400, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		self.window.gridLayout.addItem(spacer, 0, 1, 1, 1)
		self.visibleItems.append(spacer)



	def spot(self):
		'''
		'''
		#self.destroyUIbyList()
		self.destroyUIbyLayout()

		spinBox = QtGui.QSpinBox()
		self.window.gridLayout.addWidget(spinBox)
		self.visibleItems.append(spinBox)

	def marca(self):
		#self.destroyUIbyList()
		self.destroyUIbyLayout()

		lbl = QtGui.QLabel()
		lbl.setText('Marca_test')
		self.window.gridLayout.addWidget(lbl)
		self.visibleItems.append(lbl)

	def campana(self):
		#self.destroyUIbyList()
		self.destroyUIbyLayout()

		lbl = QtGui.QLabel()
		lbl.setText('Campana test')
		self.window.gridLayout.addWidget(lbl)
		self.visibleItems.append(lbl)

		


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
				if str(self.window.gridLayout.itemAt(i).item().objectName()) == '':
					itemDelete = self.window.gridLayout.itemAt(i).item()
					itemDelete.deleteLater()
					#widgetDelete.setParent(None)
				

