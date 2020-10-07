import pygame as pyg
from fileslib.libreria import *


if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([ANCHO,ALTO])

    # Dibujar poligono rotante
    grado = 2
    #puntoCirculo = getplanopos(-100,100)
    figura = [[-100,100], [-200,100], [100,150]]
    lista1punto = transformToCarte(figura)
    
    #Mi punto fijo (Con que punto va a rotar mi figura)
    puntofijo = figura[0]

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
                    
                rotacionFigura = rotacion(figura, grado)
                # En que punto de la figura mi figura va a rotar
                pf = getPuntoFijo(rotacionFigura[0], puntofijo)
                lista1punto = puntosTraslacion(rotacionFigura, pf)
                lista1punto = transformToCarte(lista1punto)
                


        #Logica
        pantalla.fill([0,0,0])
        
        
        drawplano(pantalla)
        pyg.draw.polygon(pantalla, [0,250,0], transformToCarte(figura), 1)
        pyg.draw.polygon(pantalla, [0,250,0], lista1punto, 1)

        pyg.display.flip()
        reloj.tick(60)        
                

    print("Fin del programa")        

 