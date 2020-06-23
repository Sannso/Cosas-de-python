from AbstractRetirarMonto import *

class MontoCincuenta(AbsRetirarMonto):
	def __init__(self, sucesor):
		self.__denominacion = 50000
		self.__cantidad = 1;
		self.__sucesor = sucesor;


	def retirarMonto(self, monto):
		dineroR = int(monto)
		if((dineroR/self.__denominacion) >= 0):
			contador = 0;
			for x in range(1,2):
				if((dineroR-self.__denominacion) >= 0):
					dineroR = dineroR - self.__denominacion
					contador=contador+1

			print("Se cargan " + str(contador) + " Billete(s) de 50,000\n")
		
		self.__sucesor.retirarMonto(dineroR)


