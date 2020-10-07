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


def getplanopos(x, y, escalado = [1,1], centro = CENTRO):
    newx = centro[0]+(x*escalado[0])
    newy = centro[1]+(y*(-1)*escalado[1])
    return [newx, newy]

def transformToCarte(npuntos):
    newpoints = []

    for i in npuntos:
        newpoints.append(getplanopos(i[0], i[1]))

    return newpoints

def rotacion(puntos, gr):
    newp=[]
    grados = math.radians(gr)

    for i in puntos:
        transX = (i[0] * math.cos(grados)) + ((-1) * i[1] * math.sin(grados))
        transY = (i[0] * math.sin(grados)) + (i[1] * math.cos(grados))
        newp.append([int(transX), int(transY)])

    return newp


def polarToCart(r, gr):
    newp=[]
    grados = math.radians(gr)

    newp.append(int(r * math.cos(grados)))
    newp.append(int(r * math.sin(grados)))

    return newp

def drawRosaPolar(win, a, r, g, nP):
    punto = []
    grados = math.radians(g)
    radio = a * math.cos(nP*grados)

    punto.append(int(radio * math.cos(grados)))
    punto.append(int(radio * math.sin(grados)))

    punto = getplanopos(punto[0], punto[1])
    pyg.draw.circle(win, [250,0,0], punto, 3)


def puntoTraslacion(punto, traslacion):
    newp = []
    newp.append(punto[0] + traslacion[0])
    newp.append(punto[1] + traslacion[1])
    return newp

def puntosTraslacion(puntos, traslacion):
    newp = []
    
    for i in puntos:
        x = i[0] + traslacion[0]
        y = i[1] + traslacion[1]
        newp.append([x, y])

    return newp

def getPuntoFijo(punto1, punto2):
    pf = []
    pf.append((punto1[0] - punto2[0])*(-1))
    pf.append((punto1[1] - punto2[1])*(-1))
    return pf

'''
def rotacioninverse(puntos, gr):
    newp=[]
    grados = math.radians(gr)

    for i in puntos:
        transX = (i[0] * math.cos(grados)) + (i[1] * math.sin(grados))
        transY = ((-1) *i[0] * math.sin(grados)) + (i[1] * math.cos(grados))
        newp.append([int(transX), int(transY)])

    return newp
'''

def drawplano(win, color = ROSA):
    pyg.draw.line(win, color, [int(ANCHO/2),0], [int(ANCHO/2),ALTO])
    pyg.draw.line(win, color, [0, int(ALTO/2)], [ANCHO, int(ALTO/2)])    

def drawrect(win, func, yinf, ysup):
    if(func == "recta"):
        x = ysup
        y = x
        
        while(y > yinf):
            pyg.draw.circle(win, [250,0,0], getplanopos(x,y, [1,1]), 2)
            x = x - 5
            y = x
            pyg.display.flip() 


def drawtria(win, punto):
    pyg.draw.polygon(win, [0,250,0], punto, 1)

def drawPoint(win, punto, color = VERDE):
    pyg.draw.circle(win, color, punto, 2)

def escalar(punto, escalado):
    newlist = []
    for i in punto:
        x = i[0] * escalado[0]
        y = i[1] * escalado[1]
        newlist.append([x,y])
    return newlist