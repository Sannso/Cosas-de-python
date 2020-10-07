import pygame as pyg
from fileslib.libreria import *


if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([ANCHO,ALTO])

    drawplano(pantalla)

    punto = [200, 100]
    puntotr = puntoTraslacion(punto, [-50,-100])
 
    drawPoint(pantalla, punto)
    drawPoint(pantalla, puntotr)

    puntoC = getplanopos(200, 100)
    puntotrC = getplanopos(puntotr[0], puntotr[1])

    drawPoint(pantalla, puntoC)
    drawPoint(pantalla, puntotrC, ROJO)

    #Traslacion de un triangulo
    triangulo = [[100, 100], [100, 200], [200, 250]]

    #Triangulo en cartesiano
    trianguloC = transformToCarte(triangulo)
    drawtria(pantalla, trianguloC)

    #Pasar el triangulo al centro
    trianguloT = puntosTraslacion(triangulo, [-100,-200])
    trianguloTC = transformToCarte(trianguloT)
    drawtria(pantalla, trianguloTC)

    fin = False
    while(not fin):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin = True
     
        pyg.display.flip() 
    print("Fin del programa")        

 