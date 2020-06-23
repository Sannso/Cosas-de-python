from abc import ABCMeta, abstractmethod

class IConsumo(metaclass=ABCMeta):

	@abstractmethod
	def getDatosConsumo(self): pass

