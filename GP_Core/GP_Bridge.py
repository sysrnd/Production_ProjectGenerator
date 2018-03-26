# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class GP_Bridge(object):
	def __init__(self, window):
		
		self.window = window
		QtCore.QObject.connect(self.window.cmB_type, QtCore.SIGNAL("currentIndexChanged(QString)"), self.populateUI)

		self.UIDict = {0: self.mexicartoon, 1: self.spot, 2: self.marca, 3: self.campana}

	def populateUI(self):
		functionToCall = self.UIDict[self.window.cmB_type.currentIndex()]()
		#functionToCall()
		

	def mexicartoon(self):

		print 'test'

	def spot(self):

		print 'test'

	def marca(self):
		pass

	def campana(self):
		pass