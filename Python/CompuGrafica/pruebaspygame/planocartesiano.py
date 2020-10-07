import pygame as pyg

def getplanopos(x, y, escalado, centro):
    newx = centro[0]+(x*escalado[0])
    newy = centro[1]+(y*(-1)*escalado[1])
    return [newx, newy]

def drawrect(win, func, yinf, ysup, centro):
    if(func == "recta"):
        x = ysup
        y = x
        
        while(y > yinf):
            pyg.draw.circle(pantalla, [250,0,0], getplanopos(x,y, [1,1], centro), 2)
            x = x - 5
            y = x
            pyg.display.flip() 


if __name__ == "__main__":
    pyg.init()
    # Constantes de la pantalla
    ANCHO = 1000
    ALTO = 600

    pantalla = pyg.display.set_mode([ANCHO,ALTO])

    position = [200,250]

    # Centro del plano
    CENTRO = [int(ANCHO/2),int(ALTO/2)]

    pyg.draw.line(pantalla, [0,250,0], [500,0], [500,600])
    pyg.draw.line(pantalla, [0,250,0], [0, 300], [1000, 300])

    pyg.draw.circle(pantalla, [250,0,0], getplanopos(50,50, [2,2], CENTRO), 10, 1)
    pyg.draw.circle(pantalla, [250,0,0], getplanopos(-50,50, [2,2], CENTRO), 10, 1)
    pyg.draw.circle(pantalla, [250,0,0], getplanopos(-50,-50, [2,2], CENTRO), 10, 1)
    pyg.draw.circle(pantalla, [250,0,0], getplanopos(50,-50, [2,2], CENTRO), 10, 1)

    drawrect(pantalla, "recta", -200, 200, CENTRO)

    fin = False
    while(not fin):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin = True


        pyg.display.flip()        
                

    print("Fin del programa")        

 