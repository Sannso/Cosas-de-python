import pickle


class Vehiculos():

    def __init__(self, tipo, marca, color):
        self.__Tipo = tipo
        self.__Marca = marca
        self.__Color = color
        self.__mStatus = False
        self.__Aceleracion = False

    def getTipo(self):
        return self.__Tipo

    def getMarca(self):
        return self.__Marca

    def getColor(self):
        return self.__Color

    def setColor(self, C):
        self.__Color = C

    def moveStatus(self):
        if(self.__Aceleracion == False and self.__mStatus == False):
            self.__mStatus = True

        else:
            self.__mStatus = False

    def Acelera(self):
        if(self.__Aceleracion == False and self.__mStatus == True):
            self.__Aceleracion = True

        else:
            self.__Aceleracion = False

    def Status(self):
        move = ""
        if(self.__mStatus):
            move = "en Movimento"
        else:
            move = "Aparcado"

        print("\nEl vehiculo de tipo " + self.__Tipo + " De marca " + self.__Marca + " Y color " + self.__Color + "\nSe encuentra " + move)
        return ""

"""
# Creacion del archio serializado


coche1 = Vehiculos("carro", "mazda", "rojo")
coche2 = Vehiculos("carro", "bmw", "negro")
coche3 = Vehiculos("carro", "ferrari", "amarillo")

# Para no tener que serializar, coche por coche los podemos meter en una lista

coches = [coche1, coche2, coche3]


archivo_coches= open("archivo_objetos", "wb")

pickle.dump(coches, archivo_coches)
archivo_coches.close()
del(archivo_coches)
"""

# Con el archivo creoado en la parte superior ahora vamos a leerla

archivo_coches2 = open("archivo_objetos", "rb")

mis_coches = pickle.load(archivo_coches2)
archivo_coches2.close()


for i in mis_coches:
    print(i.Status())
