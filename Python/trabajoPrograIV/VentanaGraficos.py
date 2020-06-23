from IVentana import *
from View import *

from tkinter import *
from tkinter.ttk import * 
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class VentanaGraficos(IVentana):

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
			
			self.cuadroInformacion()

			# ------------------- STYLE BUTTONS ---------------------------
			styleButtons = Style()
			styleButtons.configure('My.TButton', font=("Consolas", 16, "bold"), justify="center",
									activebackground="black", activeforeground="white")

			# ------------------- BOTON VOLVER -------------------------------
			buttonVolver = Button(self.myFrame, text="VOLVER", style="My.TButton",
								command= lambda:self.nextWindow("", 2), width="8")

			buttonVolver.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.05)

			# --------------------- GRAFICA ------------------------------------
			consu=''
			if(self.control.getPosRecolector(2).lower() == 'dias'):
				consu = 'Diario'

			elif(self.control.getPosRecolector(2).lower() == 'semanas'):
				consu = 'Semanal'

			elif(self.control.getPosRecolector(2).lower() == 'meses'):
				consu = 'Mensual'

			Label(self.myFrame, text="Consumo " + consu,
					 style="My.TLabel").place(relx=0.42, rely=0.1, relwidth=0.36, relheight=0.1)

			fig = controller.getDatosGrafico()

			canvas = FigureCanvasTkAgg(fig, self.myFrame)
			canvas.draw()
			canvas.get_tk_widget().place(relx= 0.32, rely=0.2, relwidth=0.63, relheight=0.60)
			

			toolbar = NavigationToolbar2Tk(canvas, self.myFrame)
			toolbar.update()
			toolbar.place(relx= 0.32, rely=0.80, relwidth=0.63, relheight=0.06)


			root.mainloop()



	def nextWindow(self, valor, ventana):
		self.myFrame.pack_forget()
		self.control.cargarRecolectorModelo(valor, ventana)
		self.vista.creacionV(valor, ventana)


	def cuadroInformacion(self):
		canvas = Canvas(self.myFrame, width=300, height=210, background="#FFDCD6")
		canvas.place(relx=0.02, rely=0.12, relwidth=0.2, relheight=0.2)
		#canvas.create_rectangle(10, 10, 50, 50, width=5, fill='red')

		styleLabel2 = Style()
		styleLabel2.configure('BW.TLabel', background="#FFDCD6",  font=("Consolas", 13, "bold"))

		Label(canvas, text="Usuario: " + self.control.getPosRecolector(0),
			 style="BW.TLabel").place(relx=0.02, rely=0.02, relwidth=0.8, relheight=0.25)

		Label(canvas, text="Consumo: " + self.control.getPosRecolector(1),
			 style="BW.TLabel").place(relx=0.02, rely=0.385, relwidth=0.8, relheight=0.25)

		Label(canvas, text="Horario: " + self.control.getPosRecolector(2),
			 style="BW.TLabel").place(relx=0.02, rely=0.75, relwidth=0.8, relheight=0.25)
