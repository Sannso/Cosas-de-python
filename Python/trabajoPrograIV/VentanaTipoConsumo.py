from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb 
from IVentana import *
from View import *


class VentanaTipoConsumo(IVentana):

	def __init__(self, vista, warning):
		self.vista = vista
		self.warning = warning

	def graficarInterfaz(self, root, controller):
			style = Style()
			style.configure("My.TFrame", background="#FF6347")	

			self.control = controller
			if(self.warning):
				mb.showerror("ADVERTENCIA!", "Ocurrio un error con la carga del archivo," +
				 "escoger otra opcion de consumo")

			self.myFrame = Frame(root, width="1080", height="680")
			self.myFrame.config(style="My.TFrame")
			self.myFrame.pack()

			styleLabel = Style()
			styleLabel.configure('My.TLabel', background="#FF6347",  font=("Consolas", 20, "bold"))

			Label(self.myFrame, text="Elija aqui el tipo de consumo\n 	que quiere ver",
			 style="My.TLabel").place(relx=0.30, rely=0.2, relwidth=0.5, relheight=0.1)


			self.cuadroInformacion()

			# ------------------- STYLE BUTTONS ---------------------------
			styleButtons = Style()
			styleButtons.configure('My.TButton', font=("Consolas", 16, "bold"), justify="center",
									activebackground="black", activeforeground="white")

			# ------------------- BOTON VER LUZ ------------------------------

			buttonTablaDis = Button(self.myFrame, text="Ver Luz", style="My.TButton", width="8",
									 command= lambda: self.nextWindow("Luz", 2))

			buttonTablaDis.place(relx=0.39, rely=0.4, relwidth=0.22, relheight=0.1)

			# ------------------- BOTON VER AGUA -------------------------------

			buttonTablaCon = Button(self.myFrame, text="Ver Agua", style="My.TButton", 
									 width="8", command= lambda:self.nextWindow("Agua", 2))

			buttonTablaCon.place(relx=0.39, rely=0.55, relwidth=0.22, relheight=0.1)

			# ------------------- BOTON VOLVER -------------------------------
			buttonVolver = Button(self.myFrame, text="VOLVER", style="My.TButton",
								command= lambda:self.nextWindow("", 0), width="8")

			buttonVolver.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.05)


			root.mainloop()



	def nextWindow(self, valor, ventana):
		self.myFrame.pack_forget()
		if(ventana==2):
			self.control.cargarRecolectorModelo(valor, ventana-1)
		else: self.control.cargarRecolectorModelo(valor, ventana)
		self.vista.creacionV(valor, ventana)
	

	def cuadroInformacion(self):

		canvas = Canvas(self.myFrame, width=300, height=210, background="#FFDCD6")
		canvas.place(relx=0.02, rely=0.12, relwidth=0.2, relheight=0.2)
		#canvas.create_rectangle(10, 10, 50, 50, width=5, fill='red')

		styleLabel2 = Style()
		styleLabel2.configure('BW.TLabel', background="#FFDCD6",  font=("Consolas", 13, "bold"))

		Label(canvas, text="Usuario: " + self.control.getPosRecolector(0),
			 style="BW.TLabel").place(relx=0.02, rely=0.02, relwidth=0.8, relheight=0.25)
			
