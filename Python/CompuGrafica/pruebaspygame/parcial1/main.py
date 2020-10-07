import pygame as pyg
from fileslibparcial.libreria import *


if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([ANCHO,ALTO])
    changeCentroPlano(200, 300)

    # Cuadrado
    cuadrado = [[100,100], [-100,100], [-100,-100], [100, -100]]

    # Linea separadora
    linea = [[210, 110], [210, -110]]
    linea = transformToCarte(linea)
    
    #Valores Polares
    r = getR(cuadrado[0][0], 45)
    angulo = 0

    puntosq = polarToCart(r, angulo)


    # Puntos de la grafica
    gfpoints = []

    reloj = pyg.time.Clock()

    fin = False
    while(not fin):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin = True
                
        #Logica
        pantalla.fill([0,0,0])
        
        # Objetos fijos (Plano, Cuadrado, separacion)
        drawplano(pantalla)
        pyg.draw.polygon(pantalla, [0,250,0], transformToCarte(cuadrado), 1)
        pyg.draw.line(pantalla, MOSTAZA, linea[0], linea[1])

        
        # Animación Circulo
        #pyg.draw.circle(pantalla, [250,0,0], getplanopos(puntosq[0], puntosq[1]), 1)
        
        #Linea a rotar
        pinicial = getplanopos(0, 0)
        pfinal = getplanopos(puntosq[0], puntosq[1])
        #pyg.draw.line(pantalla, ROSA, pinicial, pfinal)


        #Logica de los limites para la linea rotante
        puntosquare = getPointSquare(100, 100, puntosq[0], puntosq[1], angulo)
        psf = getplanopos(puntosquare[0], puntosquare[1])  
        pyg.draw.line(pantalla, MOSTAZA, pinicial, psf)


        #Logica grafica moviendoce
        putandmove(pantalla, gfpoints, psf[1], [linea[0][0], 300])

        #Reiniciar angulo
        if(angulo == 360):
            angulo = 0
        else:
            # Incrementador
            angulo += 1
            puntosq = polarToCart(r, angulo)

        pyg.display.flip()
        reloj.tick(60)        
                

    print("Fin del programa")        

 