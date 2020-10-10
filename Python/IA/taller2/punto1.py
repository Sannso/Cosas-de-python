import numpy as np


def trainLoss(vx,vy,w):
    e = np.dot(vx, w)
    e = e - vy
    e = e * 2
    e = np.dot(e, vx)

    sumatoria = np.sum(e)
    n = 1/np.linalg.norm(len(vx))

    resultado = n*sumatoria
    return resultado

def ciclo(vx,vy,w,n):
    result = w - n * trainLoss(vx,vy,w)
    return result


vx_1 = np.array([1,0,0])
vx_2 = np.array([1,-1,0])
vx_3 = np.array([1,1,0])
vx_4 = np.array([1,0,1])
vx_5 = np.array([1,1,1])

vy_1 = 0
vy_2 = 1/2
vy_3 = 1/2
vy_4 = 1
vy_5 = 3/2

vx = np.array([vx_1, vx_2, vx_3, vx_4, vx_5])
vy = np.array([vy_1, vy_2, vy_3, vy_4, vy_5])

w = np.array([0,1,1])

#Generacion del ciclo
w = ciclo(vx, vy, w, 0.01)
print(w)

