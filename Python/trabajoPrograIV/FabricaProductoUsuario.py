from UsuarioResidencial import *
from UsuarioIndustrial import *

class FabricaUsuario:
	@staticmethod
	def getTipoUsuario(tipoU):
		if(tipoU.lower() == "residencial"):
			return UsuarioResindencial()

		elif(tipoU.lower() == "industrial"):
			return UsuarioIndustrial()	
