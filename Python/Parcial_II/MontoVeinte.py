from AbstractRetirarMonto import *

class MontoVeinte(AbsRetirarMonto):
	def __init__(self):
		self.__denominacion = 20000
		self.__cantidad = 2;


	def retirarMonto(self, monto):
		dineroR = int(monto)
		if((dineroR/self.__denominacion) >= 0):
			contador = 0;
			for x in range(1,3):
				if((dineroR-self.__denominacion) >= 0):
					dineroR = dineroR - self.__denominacion
					contador=contador+1

			print("Se se cargan " + str(contador) + " Billete(s) de 20,000\n")

		if(dineroR != 0):
			print("\nEl cajero no puede devolver la cantidad exacta\n")
		else:
			print("\nDevolviendo el dinero cargado...")
			print("El dinero ha sido entregado!\n")	
		




