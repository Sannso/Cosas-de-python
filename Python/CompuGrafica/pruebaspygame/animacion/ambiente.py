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
GRIS=[180,180,180]

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
        self.bloques=[]
        self.ratones=[]

    def update(self):

        ls_obj = pyg.sprite.spritecollide(self,self.bloques,False)
        for b in ls_obj:
            if self.rect.right > b.rect.left and self.velx>0 :
                self.rect.right = b.rect.left
                self.velx=0

            if self.rect.left < b.rect.right and self.velx<0:
                self.rect.left = b.rect.right
                self.velx=0

            if self.rect.bottom > b.rect.top and self.vely>0:
                self.rect.bottom = b.rect.top
                self.vely=0

            if self.rect.top < b.rect.bottom and self.vely<0:
                self.rect.top = b.rect.bottom
                self.vely=0


        ls_obj = pyg.sprite.spritecollide(self,self.ratones,True)

        self.rect.x+=self.velx
        self.rect.y+=self.vely



class Bloque (pyg.sprite.Sprite):
    def __init__(self, dimension, pos):
        pyg.sprite.Sprite.__init__(self)
        self.image=pyg.Surface(dimension)
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class Raton(pyg.sprite.Sprite):
    def __init__(self, pos):
        pyg.sprite.Sprite.__init__(self)
        self.image=pyg.Surface([20,20])
        self.image.fill(GRIS)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=8
        self.vely=0
        self.bloques=[]

    def update(self):
        iscollided = False
        eleccion = [8, -8]
        ls_obj=pyg.sprite.spritecollide(self,self.bloques,False)

        for b in ls_obj:
            if self.rect.right > b.rect.left and self.velx>0 :
                self.rect.right = b.rect.left
                #self.velx=0

            elif self.rect.left < b.rect.right and self.velx<0:
                self.rect.left = b.rect.right
                #self.velx=0

            elif self.rect.bottom > b.rect.top and self.vely>0:
                self.rect.bottom = b.rect.top
                #self.vely=0

            elif self.rect.top < b.rect.bottom and self.vely<0:
                self.rect.top = b.rect.bottom
                #self.vely=0

            iscollided = True


        # Deteccion de colicion en los bordes de la pantalla
        if(self.rect.right > ANCHO or
            self.rect.left < 0 or 
            self.rect.bottom > ALTO or
            self.rect.top < 0):

            if self.velx>0 :
                self.rect.right = ANCHO

            elif self.velx<0:
                self.rect.left = 0

            elif self.vely>0:
                self.rect.bottom = ALTO

            elif self.vely<0:
                self.rect.top = 0

            iscollided = True


        # Eleccion de movimiento aleatorio del raton
        if(iscollided):
            deter = random.random()
            if(deter < 0.5):
                self.velx = -self.velx
                self.vely = -self.vely

            elif(deter <= 1 and self.velx != 0):
                self.velx = 0
                self.vely = random.choice(eleccion)

            elif(deter <= 1 and self.vely != 0):
                self.velx = random.choice(eleccion)
                self.vely = 0

                

        self.rect.x += self.velx
        self.rect.y += self.vely


if __name__ == '__main__':
    pyg.init()
    pantalla=pyg.display.set_mode([ANCHO,ALTO])

    #crear
    jugadores=pyg.sprite.Group()
    bloques=pyg.sprite.Group()
    ratones=pyg.sprite.Group()

    #objeto jugador
    j=Jugador()
    jugadores.add(j)

    #Crear bloque
    #Crear mapa del ambiente
    b0=Bloque([100,200], [400,250])
    bloques.add(b0)

    b1=Bloque([200,70], [600,570])
    bloques.add(b1)

    j.bloques=bloques

    r1=Raton([50,600])
    r1.bloques=bloques
    ratones.add(r1)

    r2=Raton([650,50])
    r2.velx=0
    r2.vely=5
    r2.bloques=bloques
    ratones.add(r2)

    j.ratones = ratones

    reloj=pyg.time.Clock()
    fin=False
    while not fin:
        #gestion de eventos
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
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


        # Actualizar pantalla
        jugadores.update()
        ratones.update()

        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        bloques.draw(pantalla)
        ratones.draw(pantalla)

        pyg.display.flip()
        reloj.tick(30)