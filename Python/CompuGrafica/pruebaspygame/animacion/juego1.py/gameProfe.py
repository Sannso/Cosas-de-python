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
        self.rect.y=ALTO-70
        self.velx=0
        self.salud=200

    def update(self):
        self.rect.x+=self.velx

class Bala(pygame.sprite.Sprite):
    def __init__(self,pos, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([10,20])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vely=0

    def update(self):
        self.rect.y+=self.vely

class Rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.velx=5
        self.temp=random.randrange(30,100)

    def update(self):
        self.temp-=1
        self.rect.x+=self.velx
        if self.rect.right >= (ANCHO-50):
            self.velx= -5
        if self.rect.right <= 70:
            self.velx= 5

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    #crear
    jugadores=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas_r=pygame.sprite.Group()
    rivales=pygame.sprite.Group()

    fuente=pygame.font.Font(None,32)

    #objeto jugador
    j=Jugador()
    jugadores.add(j)

    n=10
    for i in range(10):
        r=Rival()
        r.rect.x=random.randrange(50,(ANCHO-100))
        r.rect.y=random.randrange(50,(ALTO-120))
        rivales.add(r)

    reloj=pygame.time.Clock()
    fin=False
    fin_juego=False
    while not fin and not fin_juego:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                if event.key == pygame.K_LEFT:
                    j.velx= -5
            if event.type == pygame.KEYUP:
                j.velx=0
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion=[j.rect.x + 20, j.rect.y]
                b=Bala(posicion)
                b.vely= -8
                balas.add(b)

        #Control
        for b in balas:
            ls_col=pygame.sprite.spritecollide(b,rivales,True)
            if len(ls_col)>0:
                balas.remove(b)

            if b.rect.bottom < 0:
                balas.remove(b)

        for r in rivales:
            if r.temp <=0:
                posicion=[r.rect.x + 20, r.rect.bottom]
                b=Bala(posicion,AZUL_2)
                b.vely= 8
                balas_r.add(b)
                r.temp=random.randrange(30,100)

        for b in balas_r:
            ls_col=pygame.sprite.spritecollide(b,jugadores,False)
            if len(ls_col)>0:
                balas_r.remove(b)
                j.salud-=50
                print (j.salud)

            if b.rect.top > ALTO:
                balas_r.remove(b)


        #Refresco
        info_salud='Salud: ' + str(j.salud)
        texto=fuente.render(info_salud,True, BLANCO)
        if j.salud < 100:
            texto=fuente.render(info_salud,True, ROJO)

        if j.salud<=0:
            fin_juego=True

        jugadores.update()
        balas.update()
        balas_r.update()
        rivales.update()

        pantalla.fill(NEGRO)
        pantalla.blit(texto,[600,30])
        jugadores.draw(pantalla)
        balas.draw(pantalla)
        balas_r.draw(pantalla)
        rivales.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)

    #pantalla de fin de juego
    fuente=pygame.font.Font(None,40)
    texto=fuente.render('Fin de juego',True, BLANCO)
    balas.empty()
    balas_r.empty()
    rivales.empty()
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        pantalla.fill(NEGRO)
        pantalla.blit(texto,[500,350])
        pygame.display.flip()