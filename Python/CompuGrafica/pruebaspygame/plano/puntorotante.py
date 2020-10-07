import pygame as pyg
from fileslib.libreria import *


if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([ANCHO,ALTO])

    # Dibujar punto rotante
    grado = 2
    #puntoCirculo = getplanopos(-100,100)
    puntoCirculo = [-100,100]
    lista1punto = [puntoCirculo]
    lista1punto = [getplanopos(lista1punto[0][0], lista1punto[0][1])]

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
                    
                lista1punto = rotacion([puntoCirculo], grado)
                lista1punto = [getplanopos(lista1punto[0][0], lista1punto[0][1])]



        #Logica
        #pantalla.fill([0,0,0])
        
        
        drawplano(pantalla)
        pyg.draw.circle(pantalla, [250,0,0], lista1punto[0], 3)

        pyg.display.flip()
        reloj.tick(60)        
                

    print("Fin del programa")        

 