from tkinter import * # una de las librerias de graficos


""" Documentacion:
        https://docs.python.org/3/library/tk.html
"""


raiz = Tk()

raiz.title("Ventana de pruebas") # titulo de la ventana

raiz.resizable(1,1)
# Resive como parametro verdadero o falso, el primero para el ancho(width), y el
    # segundo para el alto(height), con el fin de si se quiere redimensionar la ventana o no

raiz.iconbitmap("gato.ico")
# el icono que se muestra en la ventana se puede cambiar por una imagen con extension .ico
    # y preferiblemente deberia estar en la misma carpeta que el archivo

# raiz.geometry("720x480") # Dimensiones de la ventana

raiz.config(bg="gray") # bg= background

""" Para que no aparezca la consola cuando se corre el programa se
 puede cambiar la extension del archivo a .pyw """

""" Todo lo que se aplica en el frame tambien sirve en la raiz """

# Ahora vamos a trabajar en un frame, que funciona como un contenedor de widgets
    # (unque un frame tambien sea una widget)

miFrame = Frame()
miFrame.pack(side="left", anchor="n") # Hay que empaquetar el frame dentro de la raiz
               # Hay varios atributos para pack, entre ellos side,
                    # que indica el lado en el que va anclado el frame a la raiz
               # Tambien exite "anchor" (n, s, e, w) que hubica el frame en uno de los puntos cardinales
               # El frame tambien se puede expandir y lo logra con 2 atributos, con expand(booleano)
                    # y con fill ("x", "y", "both", "none")


miFrame.config(bg="yellow")
    # Para que el frame se muestre en la pantalla hay que darle un tamaño

miFrame.config(width="720", height="480") # Dimensiones del frame
    # El tamaño de la raiz se comenta debido a que la raiz se adecua al tamaño del frame

miFrame.config(relief="groove") # Tambien se le puede poner un borde que trae en la libreria
miFrame.config(bd="15") # Pero para que el borde se vea hay que darle un grosor, y esto se logra con "bd"

miFrame.config(cursor="hand2")

raiz.mainloop() # el main loop es como un ciclo infinito para que la ventana permanezca abierta
