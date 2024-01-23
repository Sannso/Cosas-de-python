import configparser

archivo=configparser.ConfigParser()
archivo.read('info_mapa.txt')
print (archivo.get('info','imagen'))
print (archivo.sections())

print ("items info: ", archivo.items('info'))

for s in archivo.sections():
    print("for sections: ", s)

for i in archivo.items('.'):
    print("items sections: ", i)

print("\n ---------------- \n")

mapa=archivo.get('info','mapa')
print (mapa)
ls_filas=mapa.split('\n')
print (ls_filas)
print (ls_filas[0])
for e in ls_filas[0]:
    print (e, archivo.get(e,'col'))
