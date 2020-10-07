import pygame as pyg
from fileslib.libreria import *

if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([ANCHO,ALTO])
    drawplano(pantalla)

    pyg.draw.circle(pantalla, [250,0,0], getplanopos(-50,50, [2,2], CENTRO), 10, 1)

    #drawrect(pantalla, "recta", -200, 200)

    # ---- Dibujo de un triangulo en el plano ----
    # puntos cartesianos 
    puntos = [[100,100], [100,50], [200,50]]
    npuntos = escalar(puntos, [2,2])
        # funcion para escalar la figura (Tamaño y pos por consecuente) 
   
    npuntos = transformToCarte(npuntos)
        # funcion para pasar la figura (puntos) a sistema cartesiano

    npuntos = rotacion(npuntos, 20)
        # funcion para rotar los puntos
        # IMPORTANTE Si se rota antes de la transformacion de cartesiano
            # da al revez   

    drawtria(pantalla, npuntos)


    # -- triangulo que no esta en el plano con los mismos puntos --
    #drawtria(pantalla, puntos)


    fin = False
    while(not fin):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin = True
                


        pyg.display.flip()        
                

    print("Fin del programa")        

 