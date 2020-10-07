import pygame as pyg

# Funciones

def drawdot(win, pos, color):
    pyg.draw.circle(win, color, pos, 6)
    pyg.display.flip()


def makeInterconection(win, pos, lastpoint): 
    if(not lastPoint):
        lastPoint.append(pos)
    else:
        pyg.draw.line(win, [0,250,0], lastPoint[0], pos)
        lastPoint.clear()
        lastPoint.append(pos)
        pyg.display.flip()


def drawTriangle(win, punto1, punto2, punto3):
    puntos = [punto1, punto2, punto3]
    for i in range(3):
        if(not i==2):
            pyg.draw.line(win, [0,250,0], puntos[i], puntos[i+1])
        else:
            pyg.draw.line(win, [0,250,0], puntos[i], puntos[0])    


def drawPolygon(win, pos, listp): 
    #pyg.display.flip()

    if(pos == 0):
        for i in range(len(listp)):
            if((i+1) == len(listp)):
                pyg.draw.line(win, [0,250,0], listp[-1], listp[0]) 
            else:
                pyg.draw.line(win, [0,250,0], listp[i], listp[i+1])
    else:   
        if(not listp):
            listp.append(pos)
        else:
            win.fill([0,0,0])
            listp.append(pos)
            for i in range(len(listp)):
                if((i+1) == len(listp)):
                    pyg.draw.line(win, [0,250,0], listp[-1], listp[0]) 
                else:
                    pyg.draw.line(win, [0,250,0], listp[i], listp[i+1])
            




if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([1000,600])

    fin = False

    velx = 0
    vely = 0

    ismoving = False

    lastPoint = []
    lPointPolygon = []

    #Dibujar un triangulo
    #drawTriangle(pantalla, [100, 100], [100, 300], [250, 200])


    reloj = pyg.time.Clock()

    while(not fin):

        # Gestion de eventos
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin = True

            if event.type == pyg.MOUSEBUTTONDOWN:
                

                if event.button == 1:
                    drawdot(pantalla, event.pos, [0,0,255])

                if event.button == 2:
                    drawdot(pantalla, event.pos, [0,255,0])

                if event.button == 3:
                    drawdot(pantalla, event.pos, [255,0,0])
    
                #makeInterconection(pantalla, event.pos, lastPoint)
                drawPolygon(pantalla, event.pos, lPointPolygon)
                for i in range(len(lPointPolygon)):
                    lPointPolygon[i] = list(lPointPolygon[i])


            if event.type == pyg.KEYDOWN:                
                if event.key == pyg.K_LEFT:
                    velx = -5
                    vely = 0

                if event.key == pyg.K_RIGHT:
                    velx = 5
                    vely = 0

                if event.key == pyg.K_DOWN:
                    velx = 0
                    vely = 5

                if event.key == pyg.K_UP:
                    velx = 0
                    vely = -5

                ismoving = True

            if event.type == pyg.KEYUP:
                if ((event.key == pyg.K_LEFT) and (velx < 0)) or ((event.key == pyg.K_RIGHT) and (velx > 0)):
                    velx = 0
                    ismoving = False

                if ((event.key == pyg.K_DOWN) and (vely > 0)) or ((event.key == pyg.K_UP) and (vely < 0)):
                    vely = 0
                    ismoving = False 

                           


        # Logica del programa
        #pantalla.fill([0,0,0])
        
        # Mover polygono

        if(ismoving):
            for posmove in lPointPolygon:
                posmove[0] += velx
                posmove[1] += vely
            
            pantalla.fill([0,0,0])
            drawPolygon(pantalla, 0, lPointPolygon)


        pyg.display.flip()
        reloj.tick(60)
                

    print("Fin del programa")
    pyg.quit()    