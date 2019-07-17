from tkinter import *

root = Tk()
root.title("Ventana de ejemplo")
root.iconbitmap("gato.ico")
root.config(bg="yellow")

mFrame = Frame(root, width="720", height="480")
mFrame.pack()

# Hay una forma de organizar las cosas y es con algo llamado grid, que reemplazaria a place
# y funciona como una matriz,  la cosa es que al igual que pack no respeta dimensiones

cuadroTexto = Entry(mFrame)
cuadroTexto.grid(row = 0, column = 1)

cuadroApellido = Entry(mFrame)
cuadroApellido.grid(row = 0, column = 3)

cuadroPass = Entry(mFrame)
cuadroPass.grid(row = 1, column = 1)
cuadroPass.config(show="*")
# show sirve para que al momento de escribir no se muestre lo que estamos escribiendo sino, otra cosa


cuadroDireccion = Entry(mFrame)
cuadroDireccion.grid(row = 2, column = 1)

#----------------------------------------------
# sticky junta o pega hacia los puntos cardinales, estos puntos cardinales tambien pueden fucionarse

textoN = Label(mFrame, text="Nombre: ", pady="8", padx="8")
textoN.grid(row = 0, column = 0, sticky="e")

textoA = Label(mFrame, text="Apellido: ", pady="8", padx="8")
textoA.grid(row = 0, column = 2, sticky="e")

textoP = Label(mFrame, text="Password: ", pady="8", padx="8")
textoP.grid(row = 1, column = 0, sticky="e")

textoD = Label(mFrame, text="Direccion: ", pady="8", padx="8")
textoD.grid(row = 2, column = 0, sticky="e")




root.mainloop()
