from AbstractBuilder import *
from ClaseProducto import *

class Conector:
	__conexionBuilder = object

	def setConexionBuilder(self, concreteBuilder):
		self.__conexionBuilder = concreteBuilder

	def getConexion(self):
		return self.__conexionBuilder.getConexionBD()

	def makeConexion(self):
		self.__conexionBuilder.servidorBuild()
		self.__conexionBuilder.nombreBDBuild()
		self.__conexionBuilder.usuarioBuild()
		self.__conexionBuilder.passwordBuild()		