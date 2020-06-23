from FabricaAbstractaUsuario import *
from ConsumoLuzIndustrial import *
from ConsumoAguaIndustrial import *


class UsuarioIndustrial(FabricaAbstracta):

	def getConsumoResidencial(self, tipo):
		pass

	def getConsumoIndustrial(self, tipo):
		if(tipo.lower() == "luz"):
			return ConsumoLuzIndustrial()

		elif(tipo.lower() == "agua"):	
			return ConsumoAguaIndustrial()		