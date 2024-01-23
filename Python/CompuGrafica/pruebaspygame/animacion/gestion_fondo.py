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

        self.rect.x+=self.velx
        self.rect.y+=self.vely


if __name__ == '__main__':
    pyg.init()
    pantalla=pyg.display.set_mode([ANCHO,ALTO])

    #fondo
    fondo = pyg.image.load('image.png')
    pantalla.blit(fondo, [0,0])
    f_x=0
    f_velx=0
    f_y=0
    f_vely=0

    #crear
    jugadores=pyg.sprite.Group()

    #objeto jugador
    j=Jugador()
    jugadores.add(j)

    # dim fondo
    ancho_fondo = fondo.get_rect()[2]
    alto_fondo = fondo.get_rect()[3] 
    print(ancho_fondo)

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
                    f_velx = 5
                    f_vely = 0

                if event.key == pyg.K_RIGHT:
                    j.velx = 5
                    j.vely = 0
                    f_velx = -5
                    f_vely = 0

                if event.key == pyg.K_DOWN:
                    j.velx = 0
                    j.vely = 5
                    f_vely = -5
                    f_velx = 0

                if event.key == pyg.K_UP:
                    j.velx = 0
                    j.vely = -5
                    f_vely = 5
                    f_velx = 0

            if event.type == pyg.KEYUP:
                if (((event.key == pyg.K_LEFT) and (j.velx < 0))
                 or ((event.key == pyg.K_RIGHT) and (j.velx > 0))):
                    j.velx = 0
                    

                if (((event.key == pyg.K_DOWN) and (j.vely > 0))
                 or ((event.key == pyg.K_UP) and (j.vely < 0))):
                    j.vely = 0

                if (((event.key == pyg.K_LEFT) and (f_velx > 0))
                 or ((event.key == pyg.K_RIGHT) and (f_velx < 0))):
                    f_velx = 0

                if (((event.key == pyg.K_DOWN) and (f_vely < 0))
                 or ((event.key == pyg.K_UP) and (f_vely > 0))):
                    f_vely = 0
                    

        # Control

        if(j.rect.x > (ANCHO-150) and f_x > (ANCHO-ancho_fondo) 
            and f_velx < 0):
            f_x += f_velx
            j.velx = 0 

        if(j.rect.x < 150 and f_x < 0 and f_velx > 0):
            f_x += f_velx
            j.velx = 0 

        if(j.rect.y > (ALTO-150) and f_y > (ALTO-alto_fondo)
            and f_vely < 0):
            f_y += f_vely 
            j.vely = 0 

        if(j.rect.y < 150 and f_y < 0 and f_vely > 0):
            f_y += f_vely
            j.vely = 0      


        # Actualizar pantalla
        jugadores.update()
        pantalla.blit(fondo, [f_x,f_y])
        jugadores.draw(pantalla)

        pyg.display.flip()
        reloj.tick(30)     
