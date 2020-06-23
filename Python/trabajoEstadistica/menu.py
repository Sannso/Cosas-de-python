from tkinter import *
from tkinter.ttk import * 
from variableDiscreta import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class Menu():
	def __init__(self):
		self.root = Tk()
		self.root.title("Menu - Estadistica");
		self.root.iconbitmap("icono.ico")
		self.root.config(bg="red")
		self.root.resizable(0,0)
		self.creacionMenu()

		
	def creacionMenu(self):
		try:
			self.disFrame.pack_forget()
		except:
			print("Aun no ha sido creado el frame disFrame")	

		style = Style()
		style.configure("My.TFrame", background="#FF6347")	

		self.myFrame = Frame(self.root, width="1080", height="680")
		self.myFrame.config(style="My.TFrame")
		self.myFrame.pack()

		styleLabel = Style()
		styleLabel.configure('My.TLabel', background="#FF6347",  font=("Consolas", 20, "bold"))

		Label(self.myFrame, text="MENU ESTADISTICA",
		 style="My.TLabel").place(relx=0.39, rely=0.2, relwidth=0.4, relheight=0.1)


		# ------------------- STYLE BUTTONS ---------------------------
		styleButtons = Style()
		styleButtons.configure('My.TButton', font=("Consolas", 16, "bold"), justify="center",
								activebackground="black", activeforeground="white")

		# ------------------- BOTON VARIABLE DISCRETA ------------------------------

		buttonTablaDis = Button(self.myFrame, text="Variable Discreta", style="My.TButton",
								command=self.tablaDis, width="8")

		buttonTablaDis.place(relx=0.39, rely=0.4, relwidth=0.22, relheight=0.1)

		# ------------------- BOTON VARIABLE CONTINUA -------------------------------

		buttonTablaCon = Button(self.myFrame, text="Variable Continua", style="My.TButton", 
								 width="8")

		buttonTablaCon.place(relx=0.39, rely=0.55, relwidth=0.22, relheight=0.1)

		self.root.mainloop()



	def tablaDis(self):
		self.myFrame.pack_forget()

		style = Style()
		style.configure("My.TFrame", background="#FF6347")	


		self.disFrame = Frame(self.root, width="1080", height="680")
		self.disFrame.config(style="My.TFrame")
		self.disFrame.pack()


		# ---------------------------- 	STYLE LABELS -------------------------------
		styleLabel = Style()
		styleLabel.configure('My.TLabel', background="#FF6347",  font=("Consolas", 13, "bold"))

		styleLTxt = Style()
		styleLTxt.configure('Mytxt.TLabel', background="#FF6347",  font=("Consolas", 11, "italic"))

		# ----------------------------- STYLE BUTTONS --------------------------------
		styleButtons = Style()
		styleButtons.configure('My.TButton', font=("Consolas", 10, "bold"),	justify="center",
								activebackground="black", activeforeground="white")
		# ---------------------------------------------------------------------------------


		Label(self.disFrame, text="Tabla de frecuencia para variable Discreta",
				 style="My.TLabel").place(relx=0.01, rely=0.1, relwidth=0.36, relheight=0.1)

		# ------------------- BOTON VOLVER AL MENU -------------------------------------------
		buttonVolver = Button(self.disFrame, text="Volver al MENU", style="My.TButton",
								command=self.creacionMenu, width="8")

		buttonVolver.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.03)


		# ----------------------------- DATOS DE LA TABLA (INSTANCIA DE LA CLASE) ----------------------
		discreta = VariableDiscreta()

		print(discreta.arraysTabla())
		tablaDiscreta = discreta.arraysTabla()



		# ------------------ PRINT DE LA TABLA ---------------------------
		self.treeview = Treeview(self.disFrame, columns=("_ni", "_Ni", "_hi", "_Hi"))

		self.treeview.column("#0", width=80, minwidth = 60, stretch=False)
		self.treeview.column("_ni", width=80, minwidth = 60, stretch=False)
		self.treeview.column("_Ni", width=80, minwidth = 60, stretch=False)
		self.treeview.column("_hi", width=80, minwidth = 60, stretch=False)
		self.treeview.column("_Hi", width=80, minwidth = 60, stretch=False)

		self.treeview.heading("#0", text="Yi", anchor=W)
		self.treeview.heading("_ni", text="ni", anchor=W)
		self.treeview.heading("_Ni", text="Ni", anchor=W)
		self.treeview.heading("_hi", text="hi", anchor=W)
		self.treeview.heading("_Hi", text="Hi", anchor=W)

		# ---------------------------- Impresion de los valores de la tabla ----------------------
		filaTabla = []

		for i in range(len(tablaDiscreta[0])):
			for j in tablaDiscreta:
				filaTabla.append(j[i])
			
			# Cada posicion de la tabla se ingresa
			self.treeview.insert("", END, text=str(filaTabla[0]),
				 		values=(str(filaTabla[1]), str(filaTabla[2]), str(filaTabla[3]), str(filaTabla[4])))
			del(filaTabla[0:len(tablaDiscreta[0])])
				 	
		
				
		# ------------------------------------------------------------------------------------------------

		self.treeview.place(relx=0.0, rely=0.2, relwidth=0.4, relheight=0.4)
		

		# ---------------------------- Scrollbar vertical -------------------------------------
		vsb = Scrollbar(self.disFrame, orient="vertical", command=self.treeview.yview)
		vsb.place(relx=0.4002, rely=0.201, relheight=0.408)

		self.treeview.configure(yscrollcommand=vsb.set)
		#--------------------------------------------------------------------------------------



		# -------------------------- Scrollbar horizontal -------------------------------------
		vsb = Scrollbar(self.disFrame, orient="horizontal", command=self.treeview.xview)
		vsb.place(relx=0.001, rely=0.585, relwidth=0.398)

		self.treeview.configure(xscrollcommand=vsb.set)
		#---------------------------------------------------------------------------------------

		#---------------------------- MEDIA, MODA Y MEDIANA ------------------------------------
		media = discreta.media()
		mediana = discreta.mediana()
		moda = discreta.moda()

		Label(self.disFrame, text="MEDIA:\t {:.2f}".format(media),
				 style="Mytxt.TLabel").place(relx=0.03, rely=0.65, relwidth=0.1, relheight=0.04)

		Label(self.disFrame, text="MEDIANA: {:.2f}".format(mediana),
				 style="Mytxt.TLabel").place(relx=0.03, rely=0.69, relwidth=0.1, relheight=0.04)

		Label(self.disFrame, text="MODA:\t {:.2f}".format(moda[0]),
				 style="Mytxt.TLabel").place(relx=0.03, rely=0.73, relwidth=0.1, relheight=0.04)


		# ------------------- VARIANZA, DESVIACION, COEFICIENTE DE VARIACION ----------------
		varianza = discreta.variaza()
		desviacion = discreta.desviacion()
		c_variacion = discreta.coe_variacion()

		Label(self.disFrame, text="VARIAZA:\t {:.2f}".format(varianza),
				 style="Mytxt.TLabel").place(relx=0.2, rely=0.65, relwidth=0.17, relheight=0.04)

		Label(self.disFrame, text="DESVIACION:\t {:.2f}".format(desviacion),
				 style="Mytxt.TLabel").place(relx=0.2, rely=0.69, relwidth=0.17, relheight=0.04)

		Label(self.disFrame, text="COE. VARIACION:\t {:.2f}".format(c_variacion),
				 style="Mytxt.TLabel").place(relx=0.2, rely=0.73, relwidth=0.17, relheight=0.04)



		# ------------------- ASIMETRIA ------------------
		asimetria = discreta.asimetria()
		asString = ""

		if(asimetria > 0.05): asString = "Asimetria positiva"
		elif(asimetria < 0.05): asString = "Asimetria negativa"
		else: asString = "Simetrica"

		Label(self.disFrame, text="ASIMETRIA:\t" + asString,
				 style="Mytxt.TLabel").place(relx=0.03, rely=0.80, relwidth=0.3, relheight=0.04)


		# --------------------- GRAFICA ------------------------------------
		Label(self.disFrame, text="Grafica Histograma",
				 style="My.TLabel").place(relx=0.6, rely=0.1, relwidth=0.36, relheight=0.1)

		fig = discreta.graficatkin()

		canvas = FigureCanvasTkAgg(fig, self.disFrame)
		canvas.draw()
		canvas.get_tk_widget().place(relx= 0.46, rely=0.2, relwidth=0.48, relheight=0.45)
		

		toolbar = NavigationToolbar2Tk(canvas, self.disFrame)
		toolbar.update()
		toolbar.place(relx= 0.46, rely=0.65, relwidth=0.48, relheight=0.06)
		

		#discreta.graficaHist()


		self.root.mainloop()




menu = Menu()	