from tkinter import *

root = Tk()
root.title("Calculadora")
root.iconbitmap("gato.ico")
root.resizable(0,0)

mFrame = Frame(root, width="320", height="480")
mFrame.pack()

resultado = Label(mFrame, text="Aqui va el resultado")
resultado.grid(row="0", column="0", padx="10", pady="10")

root.mainloop()
