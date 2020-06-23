from abc import ABCMeta, abstractmethod

class FabricaAbstracta(metaclass=ABCMeta):

	@abstractmethod
	def getConsumoResidencial(self, tipo): pass

	@abstractmethod
	def getConsumoIndustrial(self, tipo): pass