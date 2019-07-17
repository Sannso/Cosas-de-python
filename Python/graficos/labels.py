from tkinter import *

""" Label sintax:
                    variableLabel= Label(contenedor, opciones)
    opciones:
            Text, Anchor, Bg, Bitmap, Bd, Front, Fg: color de fuente, width, height, image, justify...
"""

raiz = Tk()
raiz.title("ventana de pruebas")
raiz.config(bg="yellow")
raiz.iconbitmap("gato.ico")

mFrame = Frame(raiz, width="720", height="480")
mFrame.pack(side="top", anchor="n")

#-------------------------------------------------------------------------------------------
miLabel = Label(mFrame, text="Primer texto de prueba en la ventana", font=("Comic Sans Ms", 10))
miLabel.place(x="340", y="130")

Label(mFrame, text="Lo mismo que la otra etiqueta pero sin variable", fg="blue").place(x="340", y="160")

miImagen = PhotoImage(file="tenor.gif")
Label(mFrame, image=miImagen, width="240", height="280").place(x="10", y="10")
#--------------------------------------------------------------------------------------------


raiz.mainloop()
