import pygame
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

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(AMARILLO)
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=250
        self.velx=0
        self.salud=200

    def update(self):
        self.rect.x+=self.velx

class Roca(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,20])
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.vely=5

    def update(self):
        self.rect.y+=self.vely
        if self.rect.y > ALTO:
            self.vely= -5
        if self.rect.y < 0:
            self.vely= 5

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    #crear
    jugadores=pygame.sprite.Group()
    rocas=pygame.sprite.Group()

    #objeto jugador
    j=Jugador()
    jugadores.add(j)

    n=10
    for i in range(n):
        r=Roca()
        r.rect.x=random.randrange(50,1100)
        r.rect.y=random.randrange(50,750)
        rocas.add(r)

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                fin=True
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RIGHT):
                    j.velx=5
                if(event.key == pygame.K_LEFT):
                    j.velx= -5
            if(event.type == pygame.KEYUP):
                j.velx=0


        # Control
        ls_obj = pygame.sprite.spritecollide(j,rocas,False)
        for r in ls_obj:
            j.salud -= 1
            print(j.salud)

        # Actualizar pantalla
        jugadores.update()
        rocas.update()

        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        rocas.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
