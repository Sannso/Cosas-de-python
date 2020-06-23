from Controller import *
from Model import *
from View import *

modelo = Modelo()
vista = Vista()
control = Controlador(vista, modelo)
control.iniciarPrograma()
