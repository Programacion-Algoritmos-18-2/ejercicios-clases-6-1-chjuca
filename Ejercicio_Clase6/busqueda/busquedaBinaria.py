class ArregloBinario(object):			# Creamos la clase ArregloBinario

	def __init__(self,datos ):			# Constructor de la clase que recibe un parametro
		self.datos = sorted(datos)

	def agregarDatos(self,datos):		# Metodo set de la Clase
		self.datos = sorted(datos)

	def busquedaBinaria(self,elementoBusqueda):		# Metodo para realizar la busqueda Binaria
		inferior=0									# Declaramos la variable Superio
		superior=len(self.datos)-1					# La variable toma el balor de el tamaño del arreglo -1
		medio=int((inferior+superior+1)/2)			# Medio toma el valor de la suma de superio,inferio+1 dividido para 2
		ubicacion=-1								# Unicacion toma el valor de -1
		while ((inferior<=superior) and (ubicacion==-1)):	# Ciclo While para ejecutar 
			if elementoBusqueda==self.datos[medio]:			# Clase para ver si el valor buscado esta en medio
				ubicacion=medio 							# ubicacion toma el valor de medio
			else:											# Sino
				if (elementoBusqueda<self.datos[medio]):	#Condicion para ver si el valor a buscar es menor o mayor al medio
					superior= medio -1						# Recalculamos el valor de superio
				else:
					inferior = medio + 1					# Recalculamos el valor de inferior
			medio=int((inferior+superior+1)/2)		# Medio toma el valor de la suma de superio,inferio+1 dividido para 2
		return ubicacion							# devolvemos ubicacion

	def __str__(self):								# Metodo __str__ para presentar los elementos del arreglo 
		temporal=""
		for elemento in self.datos:					# Ciclo para recorrer la lista de elementos
			temporal="%s %d"%(temporal,elemento)	# Formato para presentar la lista
		return temporal								# Devolvemos la lista
					