import pygame as pyg
from fileslib.libreria import *


if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([ANCHO,ALTO])

    # Obtener coordenada
    grado = 14
    radio = 60
    punto = polarToCart(radio, grado)

    # Puntos para dibujo
    punto = getplanopos(punto[0], punto[1])
    punto_base = pyg.draw.circle(pantalla, [250,0,0], punto, 3)

    reloj = pyg.time.Clock()

    fin = False
    while(not fin):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin = True

            if event.type == pyg.MOUSEBUTTONDOWN:
                # 5 rueda abajo, 4 arriba
                if event.button == 5:
                    grado = grado + 2
                
                elif event.button == 4:
                    grado = grado - 2
                
                punto = polarToCart(radio, grado)
                punto = getplanopos(punto[0], punto[1])
        
        
        #Logica
        pantalla.fill([0,0,0])
        
        
        drawplano(pantalla)
        punto_base = pyg.draw.circle(pantalla, [250,0,0], punto, 3)

        pyg.display.flip()
        reloj.tick(60)        
                

    print("Fin del programa")        

 