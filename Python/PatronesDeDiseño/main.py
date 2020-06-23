from abc import ABCMeta, abstractmethod

class AEstado:
    __metaclass__ = ABCMeta

    @abstractmethod
    def actualizar(self): raise NotImplementedError



class Fabrica:
	def getConexion(self, tipoFabrica):
		if(tipoFabrica == "Android"):return ConexionLavado()

		elif(tipoFabrica == "IOs"): return ConexionSecado()

		else: return ConexionVacia()



class ConexionLavado(AEstado):
    def actualizar(self):
        print ('Lavado')


class ConexionSecado(AEstado):
    def actualizar(self):
        print ('Secado')


class ConexionVacia(AEstado):
    def actualizar(self):
        print ('Nada')




f = Fabrica()
producto = f.getConexion("Android")
producto.actualizar()