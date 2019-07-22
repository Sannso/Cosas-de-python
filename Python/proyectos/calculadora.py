from tkinter import *





"""

        || PROBAR CON UNA CLASE DE OPERACIONES Y CREAR UN OBJETO RESULTADO


"""






root = Tk()
root.title("Calculadora")
root.iconbitmap("gato.ico")
root.resizable(0,0)
root.config(bg="black")


#------------ Primer metodo -------------------

def primerNumero(numero):
    if(numero >= 0 or numero <= 9):
        varR.set(varR.get()+str(numero))




def intermediario():
    primerNumero(7)








framePantalla = Frame(root, width="320", height="480")
framePantalla.pack()

mFrame = Frame(framePantalla, width="320", height="420")
mFrame.pack(side="bottom")




# "Pantalla"
varR = StringVar()
resultado = Label(framePantalla, text="0", textvariable=varR)
#resultado.grid(row="0", column="0", padx="10", pady="10")
resultado.pack(pady="8", padx="8", side="right")




# Botones "CE", "C", "Borrar", "Dividir"
CE = Button(mFrame, text="CE", justify="center", width="7", height="2")
CE.grid(row="1", column="0", padx="4", pady="6" )

C = Button(mFrame, text="C", justify="center", width="7", height="2")
C.grid(row="1", column="1", padx="4", pady="6" )

Delt = Button(mFrame, text="Delt", justify="center", width="7", height="2")
Delt.grid(row="1", column="2", padx="4", pady="6" )

Dividir = Button(mFrame, text="/", justify="center", width="7", height="2")
Dividir.grid(row="1", column="3", padx="4", pady="6" )





siete = Button(mFrame, text="7", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(7))
# Botones "7", "8", "9", "X"
siete.grid(row="2", column="0", padx="4" )


ocho = Button(mFrame, text="8", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(8))
ocho.grid(row="2", column="1", padx="4")

nueve = Button(mFrame, text="9", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(9))
nueve.grid(row="2", column="2", padx="4" )

Multip = Button(mFrame, text="x", justify="center", width="7", height="2")
Multip.grid(row="2", column="3", padx="4")





# Botones "4", "5", "6", "-"
cuatro = Button(mFrame, text="4", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(4))
cuatro.grid(row="3", column="0", padx="4", pady="6" )

cinco = Button(mFrame, text="5", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(5))
cinco.grid(row="3", column="1", padx="4", pady="6")

seis = Button(mFrame, text="6", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(6))
seis.grid(row="3", column="2", padx="4", pady="6" )

Restar = Button(mFrame, text="-", justify="center", width="7", height="2")
Restar.grid(row="3", column="3", padx="4", pady="6")




# Botones "1", "2", "3", "+"
uno = Button(mFrame, text="1", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(1))
uno.grid(row="4", column="0", padx="4")

dos = Button(mFrame, text="2", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(2))
dos.grid(row="4", column="1", padx="4")

tres = Button(mFrame, text="3", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(3))
tres.grid(row="4", column="2", padx="4")

Sumar = Button(mFrame, text="+", justify="center", width="7", height="2")
Sumar.grid(row="4", column="3", padx="4")




# Botones "neg", "0", ",", "="
neg = Button(mFrame, text="neg", justify="center", width="7", height="2")
neg.grid(row="5", column="0", padx="4", pady="6" )

cero = Button(mFrame, text="0", justify="center", width="7", height="2",
                    bg="black", fg="white", command=lambda: primerNumero(0))
cero.grid(row="5", column="1", padx="4", pady="6")

coma = Button(mFrame, text=",", justify="center", width="7", height="2")
coma.grid(row="5", column="2", padx="4", pady="6" )

Igual = Button(mFrame, text="=", justify="center", width="7", height="2")
Igual.grid(row="5", column="3", padx="4", pady="6")


root.mainloop()
