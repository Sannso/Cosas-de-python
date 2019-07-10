
valor= int(input("Introduce un valor cualquiera: "))
valor2= int(input("Introduce el segundo valor: "))
print("El valor fue: ", valor + valor2)


# prueba de in
print("")
print("-- Sistema de eleccion de asignaturas --")
print("Asignaturas: Matematicas - Español - Laboratorio de física")
eleccion = input("Escoja la asignatura deseada: ")

asignatura = eleccion.lower()

if asignatura in ("matematicas", "español", "laboratorio de fisica"):
    print("Acaba de registrar: " + asignatura + " existosamente")

else:
    print("La asignatura: " + asignatura + ", NO se encuentra en el sistema")
