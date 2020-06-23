import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class VariableDiscreta():



	def __init__(self):

		self.tabla = pd.read_excel('datosTabla.xlsx', 'Hoja1')
		print(self.tabla.dtypes)

		self.tablanp = np.array(self.tabla['Datos'], dtype=float)
		print(self.tablanp.dtype)

		self.datosUnicos = pd.unique(self.tabla['Datos'])
		print(self.datosUnicos)

		print(len(self.datosUnicos))
		print(self.tabla['Datos'].nunique()) #Cuenta la cantidad de datos diferentes

		# Pasar tabla a un array
		self.datosUnicosArray = np.sort(self.datosUnicos, axis=None)
		self.arrayT = self.tabla['Datos'].to_numpy()

		#print(self.arraysTabla())


	def arraysTabla(self):
		arrayAr = []
		arrayAr.append(self.variable()) 				# Variables
		arrayAr.append(self.calculo_ni_and_Ni(True))	# ni - frecuencia absoluta
		arrayAr.append(self.calculo_ni_and_Ni(False))	# Ni - frecuencia acomulada
		arrayAr.append(self.calculo_hi())				# hi - frecuencia relativa
		arrayAr.append(self.calculo_Hi())				# Hi - frecuencia acomulada

		return arrayAr

	
	def variable(self):
		array = []
		for i in self.datosUnicosArray:
			array.append(i)

		return array	


	def calculo_ni_and_Ni(self, bool):
		arrayAux = []
		contador = 0
		for i in self.datosUnicosArray:
			for j in self.arrayT:
				if(j == i): contador+=1
			arrayAux.append(round(contador, 0))
			if(bool): contador = 0
		
		return arrayAux	


	def calculo_hi(self):
		ni = self.calculo_ni_and_Ni(True) # true es para ni, false para Ni
		tamañoDatos = len(self.arrayT)
		arrayAux = []

		for i in ni: 
			arrayAux.append(round((i/tamañoDatos),4))
		
		return arrayAux



	def calculo_Hi(self):
		hi = self.calculo_hi()
		arrayAux = []

		for i in range(len(hi)): 
			if(i == 0): arrayAux.append(hi[i])
			else:
				arrayAux.append(round(hi[i] + arrayAux[i-1], 4))

		
		return arrayAux				


	def media(self):
		media = self.tabla['Datos'].mean()
		return media

	def mediana(self):
		mediana = self.tabla['Datos'].median()
		return mediana

	def moda(self):
		# SOLO PARA VARIABLES DISCRETAS	
		moda = self.tabla['Datos'].mode()
		return moda


	def variaza(self):
		var = self.tabla['Datos'].var(ddof=0)
		return var


	def desviacion(self):
		std = self.tabla['Datos'].std(ddof=0)
		return std


	def coe_variacion(self):
		cv2 = ss.variation(self.tablanp) # No se porque pero devuelve un numpy array
		return cv2

	def asimetria(self):
		asimetria = ss.skew(self.tabla['Datos'])
		return asimetria	



	def graficaHist(self):
		names = self.variable()
		values = self.calculo_ni_and_Ni(True)
		
		plt.title("Histograma")
		#plt.bar(names, values)
		plt.hist(self.tabla['Datos'], edgecolor='black')
		plt.grid(True)
		plt.show()



	def graficatkin(self):
		
		fig = Figure(figsize=(5,4), dpi=100)
		a = fig.add_subplot(111)
		a.hist(self.tabla['Datos'], edgecolor='black')
		a.grid(True)
		return fig