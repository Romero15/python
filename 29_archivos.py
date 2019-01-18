#Archivo python
"""
La función clave para trabajar con archivos en Python es la open()función.

La open()función toma dos parámetros; nombre del archivo , y el modo .

Hay cuatro métodos diferentes (modos) para la apertura de un archivo:

	"r"- Leer - El valor por defecto. Abre un archivo para lectura, error si no existe el archivo

	"a" - Anexar - Abre un archivo para anexar, crea el archivo si no existe

	"w" - Escribir - Abre un archivo para escritura, crea el archivo si no existe

	"x" - Crear - Crea el archivo especificado, devuelve un error si existe el archivo

Además, puede especificar si el archivo debe ser manejado como el modo binario o de texto

	"t"- Texto - El valor por defecto. el modo de texto

	"b" - Binario - binario modo (por ejemplo, imágenes)


"""
try:
	f = open("demofile2.txt", "rt")
except:
	#Como el archivo no existe vamos siempre a la excepcion
	print("Ver código sobre manejo de archivos")