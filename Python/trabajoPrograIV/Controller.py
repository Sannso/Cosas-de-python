from View import *
from Model import *
from FabricaProductoUsuario import *

class Controlador():

	def __init__(self, vista, modelo):
		self.vista = vista
		self.modelo = modelo
		self.fabricaUsuario = object
		self.consumoUsuario = object


	def iniciarPrograma(self):
		self.vista.iniciarVentana(self)
		#self.vista.creacionV("", 0, self)


	def crearUsuario(self):
		consumo = object
		recolector = self.modelo.getRecolector()
		self.fabricaUsuario = FabricaUsuario().getTipoUsuario(recolector[0])

		if(recolector[0].lower() == "industrial"):
			consumo = self.fabricaUsuario.getConsumoIndustrial(recolector[1])
		
		if(recolector[0].lower() == "residencial"):
			consumo = self.fabricaUsuario.getConsumoResidencial(recolector[1])

		self.modelo.cargarDatos(consumo.getDatosConsumo())


	def cargarRecolectorModelo(self, valor, posicion):
		self.modelo.recolectarValor(valor, posicion)

	def getPosRecolector(self, pos):
		return self.modelo.getPosRecolector(pos)	

	def getDatosGrafico(self):
		return self.modelo.getDatosGrafica()
