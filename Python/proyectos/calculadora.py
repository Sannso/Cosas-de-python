from tkinter import *


"""
    Calculadora mono-operacion

    made by: Santiago Sosa
    from: Colombia
    lenguage: Python
"""

"""
    Mis sugerencias propias:

                para evitar lo de sobreescribir el resultado:
                            ninguna
"""


root = Tk()
root.title("Calculadora")
root.iconbitmap("gato.ico")
root.resizable(0,0)
root.config(bg="black")


"""----(llamado por el teclado numerico) Pone los numeros en pantalla  -----"""

def Numeros(numero):

    if( varR.get() == "0"):   # Esto es para borrar el cero que aparece por defecto cuando
        varR.set("")                        # se crea la interfaz (quiza sea use de algo mas)

    if(numero >= 0 or numero <= 9):
        varR.set(varR.get()+str(numero))





"""--- (llamado por todo menos los numeros y el igual(=) ) Operaciones con numeros ------"""

def Operaciones(ope):
    #------------------------------------------------------------------------------
    hayOperador = 0  # Variable para evitar dos operadores seguidos

    for i in varR.get():   # Mi metodo momentaneo para evitar dos operadores seguidos
        if(i == "x" or i == "/" or i == "+" or i == "-"):
            if(hayOperador == 0):
                hayOperador = 1


    if(hayOperador <= 1 and ope != "ce" and ope != "delt"):     # Verificador y el que hace el cambio de la variable que
        varR.set(varR.get() + ope)      # muestra el resultado en pantalla|

    # ----------------------------------------------------------------------------
            # Elimina el ultimo digito
    if(ope == "delt"):
        cadena = ""
        large = len(varR.get())


        if(large == 1):
            varR.set("0")

        elif(large > 1):
            contador = 0
            for i in varR.get():
                if(contador <= (large - 2)):
                    contador+=1
                    cadena = cadena + i

            varR.set(cadena)

    #-----------------------------------------------------------------------------

    if(ope == "ce"):       # Borra un bloque de numero que haya en la pantalla
        cadena = ""
        contadorO = 0

        for i in varR.get():

            if(contadorO == 0 and (i.isdigit() or i == ".")):
                cadena = cadena + i

            elif(i.isdigit() == False and i != "."):
                cadena = cadena + i
                contadorO = contadorO + 1

            elif(contadorO >= 1 and (i.isdigit() or i == ".")):
                contadorO = contadorO + 1

        if(contadorO <= 1):
            varR.set("0")

        else:
            varR.set(cadena)


    # ----------------------------------------------------------------------------

    if(ope == "c"):         # Borra todo
        varR.set("0")

    #-----------------------------------------------------------------------------

    #if(ope == "neg"):




"""----(Llamado pro el operador igual(=)) Operaciones matematicas --------"""

def hacerOperaciones():
    cadena1 = ""
    cadena2 = ""
    operador = ""
    contadorO = 0

    print(varR.get())

    for i in varR.get():

        if(contadorO == 0 and (i.isdigit() or i == ".")):
            cadena1 = cadena1 + i

        elif(i.isdigit() == False and i != "."):
                operador = i
                contadorO = contadorO + 1

        elif(contadorO == 1 and (i.isdigit() or i == ".")):
            cadena2 = cadena2 + i

    print(cadena1+"\n"+cadena2+"\n"+operador)

    if(operador == "+"):
        result = float(cadena1) + float(cadena2)
        varR.set("{0:.2f}".format(result))

    if(operador == "-"):
        result = float(cadena1) - float(cadena2)
        varR.set("{0:.2f}".format(result))

    if(operador == "/"):
        result = float(cadena1) / float(cadena2)
        varR.set("{0:.2f}".format(result))

    if(operador == "x"):
        result = float(cadena1) * float(cadena2)
        varR.set("{0:.2f}".format(result))





framePantalla = Frame(root, width="320", height="480")
framePantalla.pack()

mFrame = Frame(framePantalla, width="320", height="420")
mFrame.pack(side="bottom")




# "Pantalla"
varR = StringVar(value="0")
resultado = Label(framePantalla, textvariable=varR)
#resultado.grid(row="0", column="0", padx="10", pady="10")
resultado.pack(pady="8", padx="8", side="right")




# Botones "CE", "C", "Borrar", "Dividir"
CE = Button(mFrame, text="CE", justify="center", width="7", height="2",
                        command=lambda: Operaciones("ce"))
CE.grid(row="1", column="0", padx="4", pady="6" )

C = Button(mFrame, text="C", justify="center", width="7", height="2",
                        command=lambda: Operaciones("c"))
C.grid(row="1", column="1", padx="4", pady="6" )

Delt = Button(mFrame, text="Delete", justify="center", width="7", height="2",
                        command=lambda: Operaciones("delt"))
Delt.grid(row="1", column="2", padx="4", pady="6" )

Dividir = Button(mFrame, text="/", justify="center", width="7", height="2",
                        command=lambda: Operaciones("/"))
Dividir.grid(row="1", column="3", padx="4", pady="6" )





siete = Button(mFrame, text="7", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(7))
# Botones "7", "8", "9", "X"
siete.grid(row="2", column="0", padx="4" )


ocho = Button(mFrame, text="8", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(8))
ocho.grid(row="2", column="1", padx="4")

nueve = Button(mFrame, text="9", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(9))
nueve.grid(row="2", column="2", padx="4" )

Multip = Button(mFrame, text="x", justify="center", width="7", height="2", command=lambda: Operaciones("x"))
Multip.grid(row="2", column="3", padx="4")





# Botones "4", "5", "6", "-"
cuatro = Button(mFrame, text="4", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(4))
cuatro.grid(row="3", column="0", padx="4", pady="6" )

cinco = Button(mFrame, text="5", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(5))
cinco.grid(row="3", column="1", padx="4", pady="6")

seis = Button(mFrame, text="6", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(6))
seis.grid(row="3", column="2", padx="4", pady="6" )

Restar = Button(mFrame, text="-", justify="center", width="7", height="2", command=lambda: Operaciones("-"))
Restar.grid(row="3", column="3", padx="4", pady="6")




# Botones "1", "2", "3", "+"
uno = Button(mFrame, text="1", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(1))
uno.grid(row="4", column="0", padx="4")

dos = Button(mFrame, text="2", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(2))
dos.grid(row="4", column="1", padx="4")

tres = Button(mFrame, text="3", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(3))
tres.grid(row="4", column="2", padx="4")

Sumar = Button(mFrame, text="+", justify="center", width="7", height="2", command=lambda: Operaciones("+"))
Sumar.grid(row="4", column="3", padx="4")




# Botones "neg", "0", ",", "="
neg = Button(mFrame, text="neg", justify="center", width="7", height="2")
neg.grid(row="5", column="0", padx="4", pady="6" )

cero = Button(mFrame, text="0", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: Numeros(0))
cero.grid(row="5", column="1", padx="4", pady="6")

coma = Button(mFrame, text=",", justify="center", width="7", height="2", command=lambda: Operaciones("."))
coma.grid(row="5", column="2", padx="4", pady="6" )

Igual = Button(mFrame, text="=", justify="center", width="7", height="2", command=hacerOperaciones)
Igual.grid(row="5", column="3", padx="4", pady="6")


root.mainloop()
