#for i in ["aguapanela", "pan", "queso", "cafe", "arepa", "almojabana", "huevos"]:
#    print("Tiago quiere: " + i)


print(" -------------------- Programa de verificacion de email -------------------- ")

_email = input("Ingrese su correo electronico: ")
contador = False    # Verificador del arroba
dot = 0             # Puntos que me interesan luego del arroba, maximo 2 (uno esta reservado para el arroba)
seguidos = False    # Verificador si hay puntos seguidos
seguidocont = ""    # "Colaborador" de seguidos
dotArroba = False   # No hay punto luego de o antes del arroba

# Esto esta horriblemente mal pero oc

for i in _email:
    if(seguidocont != i):
        if(seguidocont == "." and i == "@"):
            seguidos = True
            break

        seguidocont = i

        if(i == "@"):
            contador=True
            dot+=1

        elif(i == " "):
            contador=False
            break

        elif(contador == True and i == "."):
            dot+=1

    else:
        seguidos = True
        break



if (contador == True and dot <= 3 and dot > 1 and seguidos == False):
    print("El correo ha sido ingresado exitosamente")
else:
    print("Ingrese bien un hpta correo no se hpta")
