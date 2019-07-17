from tkinter import *
from tkinter import messagebox  # Sirve para mostrar una ventana con un mensaje

#----------------------------------------------------------
def mensajeBoton():
    messagebox.showinfo("mensaje", "¿Porque lo clickeas?")
#-------------------------------------------------------------


root = Tk()
root.title("Ventana de prueba")
root.iconbitmap("gato.ico")
root.config(bg="yellow")

mFrame = Frame(root, width="1080", height="620")
mFrame.pack()

cuadroTexto = Entry(mFrame)
cuadroTexto.grid(row = 0, column = 1, sticky="w")

cuadroApellido = Entry(mFrame)
cuadroApellido.grid(row = 0, column = 3, padx="8")

cuadroText2 = Text(mFrame, width="40", height="5")
cuadroText2.grid(row = 1, column = 1, pady="8")
# Ahora le creamos un scrollbar a el cuadro Comentario (va por fuera)

scroll= Scrollbar(mFrame, command=cuadroText2.yview)
            # command es para referenciar donde va puesto el scroll
            # y yview es de y: vertical view: ver
scroll.grid(row= 1, column= 2, padx="8", pady="8", sticky="nsw")
            # Fucionandolos todos hace que se adapte al tamaño del cuadro de texto
cuadroText2.config(yscrollcommand=scroll.set)
                        # Con esta configuracion hacemos que la barra se posicione
                        # en donde nosotros nos encontramos respecto al cuadro de texto


boton = Button(mFrame, text="dont click", justify="center", command=mensajeBoton,
                width="8", activebackground="black", activeforeground="white")

        # command ejecuta la funcion que muestra el mensaje
boton.grid(row=2, column=1, pady="8")



""" Link de un monton de opciones que tiene Text (cuadro comentario)
            https://www.tutorialspoint.com/python/tk_text

    Link de un monton de opciones que tiene Button
            https://www.tutorialspoint.com/python/tk_button.htm
"""
#----------------------------------------------

textoN = Label(mFrame, text="Nombre: ", pady="8", padx="8")
textoN.grid(row = 0, column = 0, sticky="e")

textoA = Label(mFrame, text="Apellido: ", pady="8", padx="8")
textoA.grid(row = 0, column = 2, sticky="e")

textoC = Label(mFrame, text="Comentario: ", pady="8", padx="8")
textoC.grid(row = 1, column = 0, sticky="e")


root.mainloop()
