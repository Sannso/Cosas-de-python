# Cuando se habre un archivo el puntero se encuentra en el principio de todo,
# y cuando se lee el archivo el puntero se ubica en la parte final de todo,
# con seek, nosotros podemos elegir el lugar en donde se va a ubicar el puntero

archivo_texto=open("archivo.txt", "r")

print(archivo_texto.read())
#print(archivo_texto.read()) No lo va a imprimir dos veces ya que el puntero se encuentra al final.
#pero si lo reposicionamos con seek si podemos imprimir algo, nuevamente

archivo_texto.seek(20)
print("\n\n")
print(archivo_texto.read())

archivo_texto.close()

# ------------------------------------------------------------------------
print("\n\n")

archivo_texto=open("archivo.txt", "r")

archivo_texto.seek(19) # De esta forma podemos posicionar el puntero antes que el archio sea leido.
print(archivo_texto.read())

print("\n\n")
# Con el metodo read se puede hacer lo contrario que seek, en lugar de leer desde, lee hasta donde se le indique
archivo_texto.seek(0) # Solo para reposicionar y mostrar el ejemplo
print(archivo_texto.read(18))
# Y luego de esto si volvemos a leer el archivo va a empezar desde donde quedo el puntero
print("\n\n")
print(archivo_texto.read())

archivo_texto.close()

# Nota tambien podemos jugar con seek, posicionandolo usando el metodo "len" para el tamaño del archivo

# O por ejemplo con el metodo readline lee la primera fila del archivo,
# y si calculamos su tamaño y lo ponemos en un seek
        # el puntero leera a partir del fianl de la primera linea

# ------------------------------------------------------------------------
print("\n\n")

archivo_texto=open("archivo.txt", "r")

print(archivo_texto.readline())

archivo_texto.close()
