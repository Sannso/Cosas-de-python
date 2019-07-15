import pickle

lista_nombres = ["sebastian", "santiago", "david", "stefany"]

"""
# ahora creamos algo parecido a un fichero externo, pero va a ser un archivo binario

archivo_binario = open("archivo_lista", "wb") # wb = escritura binaria

pickle.dump(lista_nombres, archivo_binario) # de esta forma se escribe la informacion en el archivo

archivo_binario.close()
del(archivo_binario)
"""

# ahora vamos a leer ese archivo binario que fue creado con el codigo de la parte superior

archivo_binario2 = open("archivo_lista", "rb") # rb = leer informacion binaria

lista_de_nombres = pickle.load(archivo_binario2) # De esta forma se carga la informacion de el archivo binario

archivo_binario2.close()
del(archivo_binario2)

print(lista_de_nombres)
