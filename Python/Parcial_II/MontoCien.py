from AbstractRetirarMonto import *

class MontoCien(AbsRetirarMonto):
	def __init__(self, sucesor):
		self.__denominacion = 100000
		self.__cantidad = 2;
		self.__sucesor = sucesor;


	def retirarMonto(self, monto):
		dineroR = int(monto)

		if(dineroR < 20000 or dineroR > 290000):
			print("El cajero no esta disponible")

		elif((dineroR/self.__denominacion) >= 0):
			contador = 0;
			for x in range(1,3):
				if((dineroR-self.__denominacion) >= 0):
					dineroR = dineroR - self.__denominacion
					contador=contador+1

			print("El usuario solicito: " + monto)
			print("Se cargan " + str(contador) + " Billete(s) de 100,000\n")

		self.__sucesor.retirarMonto(dineroR)


