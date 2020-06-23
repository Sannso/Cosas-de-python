from tkinter import *
from tkinter.ttk import * 
from IVentana import *
from View import *

class VentanaTipoUsuario(IVentana):

	def __init__(self, vista):
		self.vista = vista

	def graficarInterfaz(self, root, controller):
			style = Style()
			style.configure("My.TFrame", background="#FF6347")	

			self.control = controller

			self.myFrame = Frame(root, width="1080", height="680")
			self.myFrame.config(style="My.TFrame")
			self.myFrame.pack()

			styleLabel = Style()
			styleLabel.configure('My.TLabel', background="#FF6347",  font=("Consolas", 20, "bold"))

			Label(self.myFrame, text="Elija aqui el tipo de usuario\n    que usted representa",
			 style="My.TLabel").place(relx=0.3, rely=0.2, relwidth=0.5, relheight=0.1)


			# ------------------- STYLE BUTTONS ---------------------------
			styleButtons = Style()
			styleButtons.configure('My.TButton', font=("Consolas", 16, "bold"), justify="center",
									activebackground="black", activeforeground="white")

			# ------------------- BOTON RESIDENCIA ------------------------------

			buttonTablaDis = Button(self.myFrame, text="Residencial", style="My.TButton", width="8",
									 command= lambda: self.nextWindow("Residencial", 1))

			buttonTablaDis.place(relx=0.39, rely=0.4, relwidth=0.22, relheight=0.1)

			# ------------------- BOTON INDUSTRIAL -------------------------------

			buttonTablaCon = Button(self.myFrame, text="Industrial", style="My.TButton", 
									 width="8", command= lambda:self.nextWindow("Industrial", 1))

			buttonTablaCon.place(relx=0.39, rely=0.55, relwidth=0.22, relheight=0.1)

			root.mainloop()



	def nextWindow(self, valor, ventana):
		self.myFrame.pack_forget()
		self.control.cargarRecolectorModelo(valor, 0)
		self.vista.creacionV(valor, ventana)
