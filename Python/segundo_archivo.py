mi_diccionario={"Alemania":"Berlin", "Colombia":"Bogota", "Venezuela":"Caracas", "Peru":"Lima"}

mi_diccionario["Argentina"]="Quito"  # Agregar una clave:valor más
print(mi_diccionario)

mi_diccionario["Argentina"]="Buenos Aires"  # Reescribir
print(mi_diccionario)

del mi_diccionario["Alemania"]  # Elimina un clave:valor
print(mi_diccionario)
print('') ; print('')

mi_tupla=("Alemania", "Colombia", "Venezuela", "Peru")
otro_diccionario={mi_tupla[0]:"Berlin", mi_tupla[1]:"Bogota", mi_tupla[2]:"Caracas", mi_tupla[3]:"Lima"}   # Cada valor de la tupla es una clave
print(otro_diccionario)
print(otro_diccionario["Colombia"]) # Como se puede ver se puede acceder a la "tupla" o la clave, con lo que tiene asignado respectivamente
print('') ; print('')

# Se puede agrgar una tupla como valor ej
dicci={"nombre":"Santiago", "edad":"18", "Birthday date":(5,4,2000)}
print(dicci)
print('')
print(dicci.keys())
print(dicci.values())
print("Longitud: ", len(dicci)) # Con end=""  Tampoco hace el salto de linea
