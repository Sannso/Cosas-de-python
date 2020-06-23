from abc import ABCMeta, abstractmethod

class AEstado:
    __metaclass__ = ABCMeta

    @abstractmethod
    def actulizar(self): raise NotImplementedError