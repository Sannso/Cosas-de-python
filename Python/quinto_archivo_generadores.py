
#Funcion normal

def generadorPares(limite):
    lista = []
    for i in range(limite):
        lista.append(i*2)

    return lista


limite = int(input("Ingrese el limite: "))
print(generadorPares(limite))

# -----------------------------------------------------------------------


#Funcion con Generador

def generadorPares(limite):
    for i in range(limite):
        yield i*2


limite = int(input("Ingrese el limite: "))
recorre_generador = generadorPares(limite)  # recorre_generador es el objeto generador
for i in recorre_generador:
    print(i)


# -----------------------------------------------------------------------


# Funcion de yield from (simplifica el hacer un for anidado)

#  *Ciudades quiere decir que no sabe cuantos datos va a recibir, pero sabe que es en forma de tupla
def generadorCiudades(*Ciudades):
    for ciudad in Ciudades:
        yield from ciudad


Ciudades_Generadas = generadorCiudades("Pereira", "Bogota", "Armenia", "Cartagena")

print(next(Ciudades_Generadas))
print(next(Ciudades_Generadas))
print(next(Ciudades_Generadas))
