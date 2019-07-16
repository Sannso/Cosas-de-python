import pickle

class Persona():

    def __init__(self, nombre, edad):
        self.__name = nombre
        self.__edad = edad
        print("Se ha creado una monstruosidad con el nombre de ", self.__name)

# Este metodo lo que hace es que cuando imprimamos un objeto persona aparezca una informacion predefinida
# en este metodo, ya que cuando no esta python nos imprime "codigos raros"
    def __str__(self):
        return "{} {}".format(self.__name, self.__edad)

    def getnombre(self):
        return self.__name

    def getedad(self):
        return str(self.__edad)


# Creamos una clase que se encarguue de almacenar y leer una lista con personas, para luego
# Guardar l objeto en un fichero externo

class Lista_personas():

    lista = []

    #

    def __init__(self):

        archivo_de_personas = open("archivo_personas", "ab+")
        archivo_de_personas.seek(0)

        try:
            self.lista = pickle.load(archivo_de_personas)
            print("Se cargaron {} personas del archivo externo".format(len(self.lista)))

        except:
            print("El archivo esta vacio")

        finally:
            archivo_de_personas.close()
            del(archivo_de_personas)

    def añadir_persona(self, p):
        self.lista.append(p)
        self.__guardarPersonasEnArchivoExterno()

    def mostrar_personas(self):
        for i in self.lista:
            print(i)

    def __guardarPersonasEnArchivoExterno(self):
        archivo_de_personas = open("archivo_personas", "wb")
        pickle.dump(self.lista, archivo_de_personas)
        archivo_de_personas.close()
        del(archivo_de_personas)



#persona1 = Persona("alfredo", 23)
#persona2 = Persona("sebastian", 16)


lista_de_personas = Lista_personas()
#lista_de_personas.añadir_persona(persona1)
#lista_de_personas.añadir_persona(persona2)

lista_de_personas.mostrar_personas()
