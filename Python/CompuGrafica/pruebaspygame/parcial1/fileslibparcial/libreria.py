import pygame as pyg
import math

# Constantes de la pantalla
ANCHO = 1000
ALTO = 600

# Centro del plano
CENTRO = [int(ANCHO/2),int(ALTO/2)]

#Colores
ROJO = [250, 0, 0]
VERDE = [0, 250, 0]
AZUL  = [0, 0, 250]
ROSA = [255, 194, 183]
MOSTAZA = [241, 196, 15] 
MORADO = [215, 189, 226]

def changeCentroPlano(ancho, alto):
    CENTRO[0] = ancho
    CENTRO[1] = alto


def getplanopos(x, y, escalado = [1,1], centro = CENTRO):
    newx = centro[0]+(x*escalado[0])
    newy = centro[1]+(y*(-1)*escalado[1])
    return [newx, newy]

def transformToCarte(npuntos):
    newpoints = []

    for i in npuntos:
        newpoints.append(getplanopos(i[0], i[1]))

    return newpoints


def getR(x, a):
    grados = math.radians(a)
    r = int(x/math.cos(grados))
    return r


def polarToCart(r, gr):
    newp=[]
    grados = math.radians(gr)

    newp.append(int(r * math.cos(grados)))
    newp.append(int(r * math.sin(grados)))

    return newp

def getPointSquare(a, b, x, y, angulo):
    o = math.radians(angulo)

    if((angulo > 135) and (angulo < 315)):
        a = -a
        b = -b


    if(((angulo < 45) or (angulo > 315))
    or ((angulo < 225) and (angulo > 135))):

        dx = x-a
        dr = dx/(math.cos(o))
        dy = dr*math.sin(o)

    elif(((angulo > 45) and (angulo < 135))
    or ((angulo > 225) and (angulo < 315))):

        dy = y-b
        dr = dy/(math.sin(o))
        dx = dr*math.cos(o)

    else:
        return [x, y]


    px = x-dx
    py = y-dy
    return [px, py]


def putandmove(win, lista, puntoy, base):
    basex = base[0]
    lista.append([basex, puntoy])
    
    if(lista[0][0] > 990):
        lista.pop(0)

    for i in lista:
        pyg.draw.circle(win, ROSA, [int(i[0]), int(i[1])], 1)

    for i in lista:
        i[0] = i[0]+2

    


def drawplano(win, color = ROSA):
    pyg.draw.line(win, color, [CENTRO[0],0], [CENTRO[0],ALTO])
    pyg.draw.line(win, color, [0, CENTRO[1]], [ANCHO, CENTRO[1]])    

