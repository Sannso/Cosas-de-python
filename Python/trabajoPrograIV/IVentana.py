from abc import ABCMeta, abstractmethod

class IVentana(metaclass=ABCMeta):

	@abstractmethod
	def graficarInterfaz(self): pass

	@abstractmethod
	def nextWindow(self, valor, ventana): pass
