class Vehiculos():  # Clase padre

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

    # Aca con el metodo Status solo sobreescribiria lo que estoy llamando en el status de las otras clases
    def Status(self):
        move = ""
        if(self.__mStatus):
            move = "en Movimento"
        else:
            move = "Aparcado"

        print("\nEl vehiculo de tipo " + self.__Tipo + " De marca " + self.__Marca + " Y color " + self.__Color + "\nSe encuentra " + move)
        return ""

class Moto(Vehiculos):

    def personasPosiblesM(self):
        return "Solo Pueden ir 2 personas en este vehiculo"

class Carro(Vehiculos):

    def personasPosiblesC(self):
        return "Solo Pueden ir 4 personas en este vehiculo"

class Bicimoto(Vehiculos):

    def personasPosiblesB(self):
        return "Solo Pueden ir 2 personas en este vehiculo"



print(" ---------------------- VEHICULOS ---------------------- ")

i = 0

while(i == 0):
    t = input("Ingrese el tipo de vehiculo (Moto, Carro o Bicimoto): ")
    if(t == "moto" or t == "carro" or "bicimoto"):
        i+=1

m = input("Ingrese la marca: ")
c = input("Ingrese el color del vehiculo: ")

motoDeTiago = Moto(t,m,c)
carroDeTiago = Carro(t,m,c)
bicimotoDeTiago = Bicimoto(t,m,c)

if(t == "moto"):
    print(motoDeTiago.Status())
    print(motoDeTiago.personasPosiblesM())

elif(t == "carro"):
    print(carroDeTiago.Status())
    print(carroDeTiago.personasPosiblesC())

elif(t == "bicimoto"):
    bicimotoDeTiago.__Color = "Blue"  # No lo corre porque los atributos estan privados
    bicimotoDeTiago.moveStatus()
    print(bicimotoDeTiago.Status())
    print(bicimotoDeTiago.personasPosiblesB())
