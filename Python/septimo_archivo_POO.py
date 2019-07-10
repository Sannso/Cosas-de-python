class persona():

    def __init__(self):             #constructor de la clase
        self.__Edad = 18           # Al poner el doble guion bajo es como si la variable
        self.__Hambre = True        # fuera privada de la clase
        self.__Salud = "Ok"

    def setEdad(self, year):
        self.Edad = year

    def getEdad(self):
        return self.__Edad

    def comer(self, comida):
        print("")
        print("Verificando Status de salud")
        if(comida == "si" and self.__Salud == "Ok"):
            print("")
            print("La salud esta en buen estado.")
            self.__Hambre = False
        else:
            print("")
            print("La salud NO esta en buen estado deberia chekearse su salud.")
            self.__Salud = "Not Ok"
            self.__Hambre = True

    def estado_hambre(self):
        if(self.__Hambre):
            return "Tiago tiene Hambre"
        else:
            return "Tiago esta lleno"

    def __health_status(self):
        if (self.__Salud == "Ok"):
            self.__Salud = "Not Ok"
        else:
            slef.__Salud = "Ok"     # Metodo "privado" solo se puede usar en esta clase


print(" -------------- Sistema de comidas de tiago -------------- ")
print("")

Tiago=persona() # Instanciamos el objeto con su clase

tiago_come = input("Ingrese 'si' o 'no' respectivamente si tiago comio o no: ")

Tiago.comer(tiago_come)

print("")
print(Tiago.estado_hambre())
print("La edad de tiago es: " + str(Tiago.getEdad()))
