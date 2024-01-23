import pygame
import random

ANCHO=1200
ALTO=800

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    terreno=pygame.image.load('terrenogen.png')
    info=terreno.get_rect()
    print (info)
    #parametros: posicion x, posicion y, ancho corte, alto corte
    an_t=info[2]
    al_t=info[3]
    print (an_t, al_t)
    ob_an=32
    ob_al=12

    an_sp = an_t / ob_an
    al_sp = al_t / ob_al
    print ('ancho sprite: ', an_sp)
    print ('alto sprite: ', al_sp)
    ls_cuadro=[]
    ls_terreno=[]
   
    for fila in range(ob_al):
        for col in range(ob_an):
            cuadro=terreno.subsurface(col*an_sp,fila*al_sp,an_sp,al_sp)
            ls_cuadro.append(cuadro)
        ls_terreno.append(ls_cuadro.copy())
        ls_cuadro.clear()    

    pantalla.blit(ls_terreno[3][23],[0,0])
    pygame.display.flip()
    fin=False
    while not fin :
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
