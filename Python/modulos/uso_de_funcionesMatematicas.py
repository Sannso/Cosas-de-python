#import funciones_matematicas

#result = funciones_matematicas.sumar(1, 2)
#print("\nResultado de la suma: " + str(result))

"""  ESTA ES OTRA FORMA  """

from funciones_matematicas import * # El "*" importa todas las funciones de el modulo para importar una funcion o clase,
                                    # en especifico abria que poner el nombre y ya, por ejemplo:
                                    #                                               from funciones_matematicas import sumar

result = sumar(2, 3)
print("\nResultado de la suma: " + str(result))
