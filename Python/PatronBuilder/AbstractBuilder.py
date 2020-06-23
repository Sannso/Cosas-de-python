from ClaseProducto import *
from abc import ABCMeta, abstractmethod

class ConexionBuilder(metaclass=ABCMeta):

	_conexionBd = object

	def __init__(self):
		self._conexionBd = ConexionBD()

	def getConexionBD(self):
		return self._conexionBd


	@abstractmethod
	def servidorBuild(self): pass

	@abstractmethod
	def nombreBDBuild(self): pass

	@abstractmethod
	def usuarioBuild(self): pass

	@abstractmethod
	def passwordBuild(self): pass
		

