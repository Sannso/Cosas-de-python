import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class Modelo():

	def __init__(self):
		self.recolectorOpciones = ["", "", ""] # "TipoUsuario", "TipoConsumo", "Horario"
		self.datos = object

	def recolectarValor(self, valor, posicion):
		self.recolectorOpciones[posicion] = valor


	def cargarDatos(self, consumo):
		self.tabla = pd.read_csv(consumo, names=['fechas', 'consumo'])
		print(self.tabla)
		#arrayConsumo = self.tabla['consumo'].to_numpy()
		self.arrayConsumo = np.array(self.tabla['consumo'], dtype=float)
		self.arrayFecha = self.tabla['fechas'].to_numpy()
		#print(self.tabla.head())
		

	def getDatosGrafica(self):
		# Diario promediar el cada dia por 1 semana
		# Semanal promediar cada dia por 1 semana y promediar esa semana, por 1 mes
		# Mensual promediar las semanas por 1 mes
		self.arFecha = []
		self.arValor = []
		self.fig = Figure(figsize=(5,4), dpi=100)
		self.a = self.fig.add_subplot(111)


		if(self.recolectorOpciones[2].lower() == "dias"):
			self.diasDatos()
			return self.fig

		elif(self.recolectorOpciones[2].lower() == "semanas"):
			self.semanasDatos()
			return self.fig	

		elif(self.recolectorOpciones[2].lower() == "meses"):
			self.mesesDatos()
			return self.fig


	def diasDatos(self):
		primerDia = ''
		arrayDias = []

		for i in self.arrayFecha[0]:
			if(i == '/'): break
			primerDia += i

		#print("Primer dia: " + "_" + primerDia + "_")
		#------------------------------------------------
		promValores = []
		dia = primerDia

		contador = 0;
		for i in self.arrayFecha:
			if(self.obtenerDia(i) != dia):
				self.agregarDia(promValores, i)
				dia = self.obtenerDia(i)
				promValores = []

			promValores.append(self.arrayConsumo[contador])
			contador += 1 

		# ---- Contruccion grafico -------
		self.a.plot(self.arFecha, self.arValor)
		self.a.grid(True)
		self.a.tick_params('x', labelrotation=90)

	
	def semanasDatos(self):
		primerDia = ''
		arrayDias = []

		for i in self.arrayFecha[0]:
			if(i == '/'): break
			primerDia += i

		#print("Primer dia: " + "_" + primerDia + "_")
		#------------------------------------------------
		promValores = []
		dia = primerDia

		contador = 0;
		contadorDias = 1;
		for i in self.arrayFecha:
			
			if(self.obtenerDia(i) != dia):
				#self.agregarDia(promValores, i)
				dia = self.obtenerDia(i)
				contadorDias += 1

			if(contadorDias == 8):
				self.agregarSemana(promValores, i)
				contadorDias = 1
				promValores = []

			promValores.append(self.arrayConsumo[contador])
			contador += 1 

		# ---- Contruccion grafico -------
		self.a.bar(self.arFecha, self.arValor)
		self.a.grid(True)
		#self.a.set_xticks(self.arFecha)
		self.a.tick_params('x', labelrotation=90)



	def mesesDatos(self):
		primerMes = ''
		arrayMeses = []

		contames = 0
		for i in self.arrayFecha[0]:
			if(contames > 0 and  i != '/'):
				primerMes += i
			if(i == '/'): contames+=1
			if(i == '/' and contames == 2): break	

		#------------------------------------------------
		promValores = []
		mes = primerMes
		contador = 0;
		contadorMeses = 1;
		for i in self.arrayFecha:
			if(self.obtenerMes(i) != mes):
				self.agregarMes(promValores, contadorMeses)
				mes = self.obtenerMes(i)
				contadorMeses += 1

			promValores.append(self.arrayConsumo[contador])
			contador += 1 

		if(contadorMeses == 2):
			self.agregarMes(promValores, contadorMeses)

		# ---- Contruccion grafico -------
		self.a.bar(self.arFecha, self.arValor)
		self.a.grid(True)
		#self.a.set_xticks(self.arFecha)
		self.a.tick_params('x', labelrotation=10)



	def agregarDia(self, valor, fecha):
		e_dataframe = pd.DataFrame(valor) 
		self.arValor.append(e_dataframe.mean())

		newfecha = ''
		for dia in fecha:
			if(dia == ' '): break 
			newfecha += dia

		self.arFecha.append(newfecha)



	def agregarSemana(self, valor, fecha):
		e_dataframe = pd.DataFrame(valor) 
		self.arValor.append(float(e_dataframe.mean()))

		newfecha = ''
		for dia in fecha:
			if(dia == ' '): break 
			newfecha += dia


		self.arFecha.append(newfecha)	



	def agregarMes(self, valor, fecha):
		e_dataframe = pd.DataFrame(valor) 
		self.arValor.append(float(e_dataframe.mean()))

		self.arFecha.append('Mes ' + str(fecha))


	def obtenerDia(self, fecha):
		dia = ''
		for i in fecha:
			if(i == '/'): break
			dia += i

		return dia	


	def obtenerMes(self, fecha):
		mes = ''
		contames = 0
		for i in fecha:
			if(contames > 0 and  i != '/'):
				mes += i
			if(i == '/'): contames+=1
			if(i == '/' and contames == 2): break		

		return mes	


	def getRecolector(self):
		return self.recolectorOpciones

	def getPosRecolector(self, pos):
		return self.recolectorOpciones[pos]













#modelo = Modelo()
#modelo.cargarDatos()