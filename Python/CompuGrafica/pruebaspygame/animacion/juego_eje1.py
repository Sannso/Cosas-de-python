import pygame as pyg
import random

ANCHO=1200
ALTO=800

VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
AMARILLO=[255,255,0]
AZUL_2=[0,255,255]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

class Jugador(pyg.sprite.Sprite):
    def __init__(self):
        pyg.sprite.Sprite.__init__(self)
        self.image=pyg.Surface([50,50])
        self.image.fill(AMARILLO)
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=250
        self.velx=0
        self.vely=0
        self.salud=200

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely


class Bloque(pyg.sprite.Sprite):

    def __init__(self, dim, pos):
        pyg.sprite.Sprite.__init__(self)
        self.image=pyg.Surface(dim)
        self.image.fill(AZUL_2)
        self.rect=self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


if __name__ == '__main__':
    pyg.init()
    pantalla=pyg.display.set_mode([ANCHO,ALTO])

    #crear
    jugadores = pyg.sprite.Group()
    bloques = pyg.sprite.Group()

    #objeto jugador
    j=Jugador()
    jugadores.add(j)

    #Creacion bloque
    b = Bloque([100, 200], [400, 250])
    bloques.add(b)

    reloj=pyg.time.Clock()
    fin=False
    while not fin:
        #gestion de eventos
        for event in pyg.event.get():
            if(event.type == pyg.QUIT):
                fin=True

            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    j.velx = -5
                    j.vely = 0

                if event.key == pyg.K_RIGHT:
                    j.velx = 5
                    j.vely = 0

                if event.key == pyg.K_DOWN:
                    j.velx = 0
                    j.vely = 5

                if event.key == pyg.K_UP:
                    j.velx = 0
                    j.vely = -5

            if event.type == pyg.KEYUP:
                if (((event.key == pyg.K_LEFT) and (j.velx < 0))
                 or ((event.key == pyg.K_RIGHT) and (j.velx > 0))):
                
                    j.velx = 0

                if (((event.key == pyg.K_DOWN) and (j.vely > 0))
                 or ((event.key == pyg.K_UP) and (j.vely < 0))):

                    j.vely = 0


        # Control
        ls_obj = pyg.sprite.spritecollide(j, bloques, False)

        for b in ls_obj:
            if( j.rect.right > b.rect.left ):
                j.rect.right = b.rect.left
                j.velx = 0


        # Actualizar pantalla
        jugadores.update()

        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        bloques.draw(pantalla)
        pyg.display.flip()
        reloj.tick(30)
