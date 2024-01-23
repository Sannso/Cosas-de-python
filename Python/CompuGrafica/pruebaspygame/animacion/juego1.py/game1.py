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
        self.rect.x=300
        self.rect.y=650
        self.velx=0
        self.vely=0
        self.salud=200

    def update(self):

        self.rect.x+=self.velx
        self.rect.y+=self.vely



class Enemy(pyg.sprite.Sprite):
    def __init__(self):
        pyg.sprite.Sprite.__init__(self)
        self.image=pyg.Surface([50,40])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()

        #Posicion aleatoria
        posx = int(random.random() * 1100)
        posy = int(random.random() * 500)
        self.rect.x=posx
        self.rect.y=posy
        self.velx=4
        self.salud=100
        self.temp = random.randrange(30,100)

    def update(self):

        # Logic
        self.temp -= 1
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            self.velx = -self.velx

        if self.rect.left < 0:
            self.rect.left = 0
            self.velx = -self.velx

        self.rect.x+=self.velx


class Bala(pyg.sprite.Sprite):
    def __init__(self, pos, color = BLANCO):
        pyg.sprite.Sprite.__init__(self)
        self.image=pyg.Surface([5,10])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vely=-8
        self.damage = 100
        self.enemies = []
        self.players = []

    def update(self):
        # Collides balas->enemy
        if(self.enemies):
            collide = pyg.sprite.spritecollide(self,self.enemies,False)
            if(collide):
                collide[0].remove(enemies) #Lo mismo que poner true
                self.remove(balas)

        # Collides balas->player
        if(self.players):
            collide = pyg.sprite.spritecollide(self,self.players,False)
            if(collide):
                print(collide[0].salud)

        self.rect.y+=self.vely


if __name__ == '__main__':
    pyg.init()
    pantalla=pyg.display.set_mode([ANCHO,ALTO])

    #fuente
    fuente = pyg.font.Font(None, 32)

    #crear
    jugadores=pyg.sprite.Group()
    balas=pyg.sprite.Group()
    enemies = pyg.sprite.Group()
    balas_ene =  pyg.sprite.Group()

    #objeto jugador
    j=Jugador()
    jugadores.add(j)

    #enemigos
    for i in range(0,4):
        x = Enemy()
        enemies.add(x)


    reloj=pyg.time.Clock()
    fin=False
    while not fin:
        #gestion de eventos
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin=True
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_a:
                    j.velx = -5
                    j.vely = 0

                if event.key == pyg.K_d:
                    j.velx = 5
                    j.vely = 0

                if event.key == pyg.K_s:
                    j.velx = 0
                    j.vely = 5

                if event.key == pyg.K_w:
                    j.velx = 0
                    j.vely = -5

            if event.type == pyg.KEYUP:
                if (((event.key == pyg.K_a) and (j.velx < 0))
                 or ((event.key == pyg.K_d) and (j.velx > 0))):
                    j.velx = 0
                    

                if (((event.key == pyg.K_s) and (j.vely > 0))
                 or ((event.key == pyg.K_w) and (j.vely < 0))):
                    j.vely = 0

            if event.type == pyg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = [int((j.rect.x+(j.rect[2])/2)-3), j.rect.y]
                    bala = Bala(position)
                    bala.enemies = enemies
                    balas.add(bala)

                    

        # Control
        #ls_obj = pyg.sprite.spritecollide(self,self.bloques,False)
        for b in balas:
            if b.rect.bottom < 0:
                balas.remove(b)


        for r in enemies:
            if r.temp <=0:
                posicion=[r.rect.x + 20, r.rect.bottom]
                b=Bala(posicion,AZUL_2)
                b.vely= 8
                b.players = jugadores
                balas_ene.add(b)
                r.temp=random.randrange(30,100)



        # Actualizar pantalla
        info_salud = 'Salud: ' + str(j.salud)
        texto = fuente.render(info_salud, True, BLANCO)
        jugadores.update()
        balas.update()
        enemies.update()
        balas_ene.update()

        pantalla.fill(NEGRO)
        pantalla.blit(texto, [550, 30])

        jugadores.draw(pantalla)
        balas.draw(pantalla)
        enemies.draw(pantalla)
        balas_ene.draw(pantalla)

        pyg.display.flip()
        reloj.tick(30)     
