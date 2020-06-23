from AbstractBuilder import *
from ClaseProducto import *

class SqlBuilder(ConexionBuilder):

	def __init__(self):
		ConexionBuilder._conexionBd = ConexionBD()


	def servidorBuild(self):
		super()._conexionBd.setServidor("Servidor SQL")


	def nombreBDBuild(self):
		super()._conexionBd.setNombreBD("Nombre instancia SQL")


	def usuarioBuild(self):
		super()._conexionBd.setUsuario("Usuario SQL")


	def passwordBuild(self):
		super()._conexionBd.setPassword("Password SQL")
