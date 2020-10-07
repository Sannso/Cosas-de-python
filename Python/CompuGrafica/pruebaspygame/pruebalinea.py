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




if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([1000,600])

    fin = False

    posx = 200
    velx = 0

    posy = 200
    vely = 0

    # -- Bool pj que uso --
    usecircle = True
    useline = False

    lastPoint = []


    drawTriangle(pantalla, [100, 100], [100, 300], [250, 200])


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
    
                makeInterconection(pantalla, event.pos, lastPoint)    

            if event.type == pyg.KEYDOWN:      
                
                if event.key == pyg.K_c:
                    usecircle = not usecircle
                    useline = not useline

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

            if event.type == pyg.KEYUP:
                if ((event.key == pyg.K_LEFT) and (velx < 0)) or ((event.key == pyg.K_RIGHT) and (velx > 0)):
                    velx = 0

                if ((event.key == pyg.K_DOWN) and (vely > 0)) or ((event.key == pyg.K_UP) and (vely < 0)):
                    vely = 0
        


        # Logica del programa
        #pantalla.fill([0,0,0])
        
        if(usecircle):
            #pyg.draw.circle(pantalla, [250,0,0], [posx,posy], 4)
            pyg.draw.rect(pantalla, [250,0,0], pyg.Rect(posx, posy, 5, 5))
        else:
            pyg.draw.line(pantalla, [0,250,0], [100, 100], [posx,posy])
        
        posx += velx
        posy += vely
        
        pyg.display.flip()
        reloj.tick(60)
                

    print("Fin del programa")
    pyg.quit()    