from busqueda.busquedaBinaria import *				# Importamos los modulos crados para llamar a las clases
from miArchivo.MiArchivo import *

enteroAbuscar=3										# Declaramos el numero a buscar
 
archivo= MiArchivo()								# Creamos un archivo tipo MiArchivo

data= archivo.obtener_informacion()					# Llamamaos a la funcion obtener_informacion
data=([l.split(",") for l in data])					# Dividimos la cadena por el caracter ","
datos=[]									# Creamos una lista vacia para guardar los elementos
for i in data:								# Recorremos el arreglo
	for j in i:								# Recorremos los elementos del arreglo anterior
		datos.append(int(j))				# Convertimos cada elemento en entero y lo agregamos a la lista vacia 

BusquedaBinaria=ArregloBinario(datos)		# Creamos un objeto de tipo BusquedaBinaria
print(BusquedaBinaria)						# Presentamos el Objeto

posicion=BusquedaBinaria.busquedaBinaria(enteroAbuscar)		# Almacecnamos en posicion lo que devuelva la funcion busquedaBinaria y le enviamos el valor a buscar

if posicion==-1:											# Condicion que permite determinar si el elemento fue encontrado o no 
	print("El entero %d no se encontro\n"%(enteroAbuscar))
else:
	print("El entero %d se encontro en la posicion %d\n"%(enteroAbuscar,posicion))