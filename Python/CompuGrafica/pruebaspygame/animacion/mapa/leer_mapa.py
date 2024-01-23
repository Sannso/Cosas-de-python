import pygame
import configparser

ANCHO=1200
ALTO=800

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    archivo=configparser.ConfigParser()
    archivo.read('info_mapa.txt')
    nom_imagen=archivo.get('info','imagen')
    terreno=pygame.image.load(nom_imagen)
    info=terreno.get_rect()

    an_t=info[2]
    al_t=info[3]

    ob_an= int (archivo.get('info','can_ancho'))
    ob_al= int (archivo.get('info','can_alto'))

    an_sp = an_t / ob_an
    al_sp = al_t / ob_al
    print ('ancho sprite: ', an_sp)
    print ('alto sprite: ', al_sp)

    ls_t=[]
    for col in range(ob_an):
        cuadro=terreno.subsurface(col*an_sp,0,an_sp,al_sp)
        ls_t.append(cuadro)


    mapa=archivo.get('info','mapa')
    ls_filas=mapa.split('\n')

    con=0
    for e in ls_filas[2]:
        col=int(archivo.get(e,'col'))
        print( e, archivo.get(e,'col'))
        pantalla.blit(ls_t[col],[con*an_sp,100])
        con+=1

    #pantalla.blit(ls_t[0],[0,0])
    pygame.display.flip()
    fin=False
    while not fin :
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
