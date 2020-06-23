from MontoVeinte import *
from MontoCincuenta import *
from MontoCien import *

print(" ------------ Cajero Automatico ---------")
print("\nIngrese su valor a retirar: ")
valor = input()

veinte = MontoVeinte()
cincu = MontoCincuenta(veinte)
cien = MontoCien(cincu)

cien.retirarMonto(valor)