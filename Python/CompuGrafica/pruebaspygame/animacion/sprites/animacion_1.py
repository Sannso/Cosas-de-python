import pygame as pyg
from lib_sprite.libreria import *

if __name__ == '__main__':
    pyg.init()
    pantalla=pyg.display.set_mode([ANCHO,ALTO])
    
    m = recortar('animales.png', [12,8])

    con = 0
    reloj = pyg.time.Clock()
    fin=False
    while not fin :
        #gestion de eventos
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin=True

        pantalla.fill(NEGRO)

        #m[fila][columna]
        pantalla.blit(m[0], [100,100])
        pyg.display.flip()
        reloj.tick(30)

        if con < 2:
            con+=1
        else:
            con = 0