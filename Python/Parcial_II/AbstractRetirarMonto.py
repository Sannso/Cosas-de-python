from abc import ABCMeta, abstractmethod

class AbsRetirarMonto(metaclass=ABCMeta):

	@abstractmethod
	def retirarMonto(self, monto): pass