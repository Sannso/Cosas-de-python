class ConexionBD:
	def __init__(self):
		self.__servidor = ""
		self.__nombreBD = ""
		self.__usuario = ""
		self.__password = ""


	def setServidor(self, servidor):
		self.__servidor = servidor 

	def getServidor(self):
		return self.__servidor

	def setNombreBD(self, bD):
		self.__nombreBD = bD

	def getNombreBD(self):
		return self.__nombreBD

	def setUsuario(self, usuario):
		self.__usuario = usuario

	def setPassword(self, password):
		self.__password = password		    