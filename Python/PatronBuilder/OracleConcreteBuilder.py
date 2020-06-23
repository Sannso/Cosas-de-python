from AbstractBuilder import *
from ClaseProducto import *

class OracleBuilder(ConexionBuilder):

	def __init__(self):
		ConexionBuilder._conexionBd = ConexionBD()

	def servidorBuild(self):
		super()._conexionBd.setServidor("Servidor Oracle")


	def nombreBDBuild(self):
		super()._conexionBd.setNombreBD("Nombre instancia Oracle")


	def usuarioBuild(self):
		super()._conexionBd.setUsuario("Usuario Oracle")


	def passwordBuild(self):
		super()._conexionBd.setPassword("Password Oracle")
