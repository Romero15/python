#Escribir Archivo python
"""
Para escribir en un archivo existente, debe agregar un parámetro a la open()función:

"x" - Crear - creará un archivo, devuelve un error si el archivo existe

"a" - Anexar - anexará al final del archivo / crea archivo si no existe

"w" - Escribir - sobrescribirá cualquier contenido existente / crea archivo si no existe
"""

f = open("demofile.txt", "a")
f.write("Now the file has one more line!") 
print("Creo un archivo myfile vacio")
f = open("myfile.txt", "x")
print("Creo un archivo myfile2 si no existe")
f = open("myfile.txt", "w")