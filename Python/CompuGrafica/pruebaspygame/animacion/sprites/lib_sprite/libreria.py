import pygame

ANCHO=1200
ALTO=800

ROJO = [250, 0, 0]
VERDE = [0, 250, 0]
AZUL  = [0, 0, 250]
ROSA = [255, 194, 183]
MOSTAZA = [241, 196, 15] 
MORADO = [215, 189, 226]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

def recortar(imagen, objdim):
    terreno=pygame.image.load(imagen)
    #parametros: posicion x, posicion y, ancho corte, alto corte
    info=terreno.get_rect()
    an_t=info[2]
    al_t=info[3]
    ob_an=objdim[0]
    ob_al=objdim[1]

    an_sp = an_t / ob_an
    al_sp = al_t / ob_al
    ls_t=[]
    for col in range(ob_an):
        cuadro=terreno.subsurface(col*an_sp,0,an_sp,al_sp)
        ls_t.append(cuadro)
        
    return ls_t
