from FabricaAbstractaUsuario import *
from ConsumoAguaResidencial import *
from ConsumoLuzResidencial import *

class UsuarioResindencial(FabricaAbstracta):

	def getConsumoResidencial(self, tipo):
		if(tipo.lower() == "luz"):
			return ConsumoLuzResidencial()

		elif(tipo.lower() == "agua"):	
			return ConsumoAguaResidencial()
	
	def getConsumoIndustrial(self, tipo):
		pass	