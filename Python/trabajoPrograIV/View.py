from tkinter import *
from tkinter.ttk import * 
from IVentana import *
from VentanaTipoUsuario import *
from VentanaTipoConsumo import *
from VentanaHorario import *
from VentanaGraficos import *

class Vista():
	def __init__(self):
		self.ventana = VentanaTipoUsuario(self)
		self.root = Tk()
		self.root.title("PL Services");
		#self.root.iconbitmap("icono.ico")
		self.root.config(bg="red")
		self.root.resizable(0,0)


	def iniciarVentana(self, controller):
		self.controller = controller
		self.creacionV("", 0)


	def creacionV(self, valor, vent):
		
		if(vent == 0):
			self.ventana = VentanaTipoUsuario(self)

		elif(vent == 1):
			self.ventana = VentanaTipoConsumo(self, False)

		elif(vent == 2):
			try:
				self.controller.crearUsuario()
				self.ventana = VentanaHorario(self)
			except:
				self.ventana = VentanaTipoConsumo(self, True)
			

		elif(vent == 3):
			self.ventana = VentanaGraficos(self)	

		self.ventana.graficarInterfaz(self.root, self.controller)	





