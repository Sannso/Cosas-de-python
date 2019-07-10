class Carro():

    def desplazamiento(self):
        print("\nMe muevo con 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("\nMe muevo con 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("\nMe muevo con 6 ruedas")


# Segun el cucho aqui es donde esta el polimorfismo, porque a la funcion no hay que especificarle
# Que tipo de dato esta resiviendo...
def desplazamiento(Vehiculo):
    Vehiculo.desplazamiento()

carrito = Carro()
desplazamiento(carrito)

bike = Moto()
desplazamiento(bike)

cami = Camion()
desplazamiento(cami)
