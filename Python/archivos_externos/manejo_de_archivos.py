from io import open  # open: creacion y apertura del archio

"""
archivo_de_texto=open("archivo.txt", "w") # open( nombre_del_archivo, forma_en_la_que_se_abre_el_archivo )
                                                # Modos de lectura:
                                                    # -lectura(r): para solo leer
                                                    # -Escritura(w): para agregar informacion a un archivo
                                                    # -Append(a): para agregar informacion a un archivo existente
frase = "Excelente dia para estudiar python \n Un sabado"

archivo_de_texto.write(frase) # Luego de haber agregado informacion al archivo hay que cerrarlo con el metodo close
archivo_de_texto.close()
"""

archivo_de_texto=open("archivo.txt", "r")

lectura=archivo_de_texto.read()
archivo_de_texto.close()

print(lectura)
print("\n\n")

archivo_de_texto=open("archivo.txt", "r")

lineas_de_texto = archivo_de_texto.readlines() #readlines guarda la informacion en forma de lista en la variable
archivo_de_texto.close()

print(lineas_de_texto)
print(len(lineas_de_texto[0]))
print("\n")

# Hago una funcion que edite el archio solo cuando yo la llame para no estar editando cada vez que corro el programa

def archivo_edit():
    archivo_de_texto=open("archivo.txt", "a")

    agrega="\nEsto se agrego con la edicion"
    archivo_de_texto.write(agrega)
    archivo_de_texto.close()

#archivo_edit()  #con esta linea se edita el archivo
