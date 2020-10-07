import pygame as pyg

if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([1000,600])

    fin = False

    posx = 200
    velx = 0

    posy = 200
    vely = 0

    reloj = pyg.time.Clock()

    while(not fin):

        # Gestion de eventos
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin = True

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

            if event.type == pyg.KEYUP:
                if ((event.key == pyg.K_LEFT) and (velx < 0)) or ((event.key == pyg.K_RIGHT) and (velx > 0)):
                    velx = 0

                if ((event.key == pyg.K_DOWN) and (vely > 0)) or ((event.key == pyg.K_UP) and (vely < 0)):
                    vely = 0
        


        # Logica del programa
        pantalla.fill([0,0,0])
        
        pyg.draw.circle(pantalla, [250,0,0], [posx,posy], 20, 1)
        posx += velx
        posy += vely
        
        pyg.display.flip()
        reloj.tick(60)
                

    print("Fin del programa")    