
archivo_texto=open("archivo.txt", "r+") # De esta forma podemos leer y escribir archivos al mismo tiempo
# A continuacion vamos a moificar la segunda linea del archivo mientras usamos read y write

""" En algun lado hay un error un no me permite ejecutarlo correctamente """

print(archivo_texto.read())

archivo_texto.seek(0)
texto_nuevo = archivo_texto.readlines()
texto_nuevo[1] = "Un sabado no, todos los dias. \n"

archivo_texto.seek(0)
archivo_texto.writelines(texto_nuevo)

archivo_texto.seek(0)
print("\n")
print(archivo_texto.read())

print("\n1ra lista")
print(texto_nuevo)
print("\n")
archivo_texto.close()

print("\n\nRestaurando el archivo...")

#-----------------------------------------------------------------------------
""" Para revisar porque al archivo le vale mucha verga y no elimina lo que tiene que eliminar """

archivo_texto=open("archivo.txt", "r+")

texto_nuevo2 = archivo_texto.readlines()

print("\n2da lista")
print(texto_nuevo2)
print("\n")

texto_nuevo2[1] = "Un sabado \n"
texto_nuevo2[2] = "Esto se reedito \n"

print("\n2da lista")
print(texto_nuevo2)
print("\n")



for i in range(len(texto_nuevo2)):
    if(i > 2):
        texto_nuevo2[i]=""


print("\n2da lista con for")
print(texto_nuevo2)
print("\n")


texto_completo=""
for i in texto_nuevo2:
    texto_completo = texto_completo + i

print(texto_completo)


archivo_texto.seek(0)
archivo_texto.write(texto_completo)

archivo_texto.seek(0)
print("\n")
print(archivo_texto.read())

archivo_texto.close()
