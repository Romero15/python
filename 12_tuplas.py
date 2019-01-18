#tuplas python
#Una tupla es una colección que es ordenado y inmutable . En Python tuplas se escriben con paréntesi
"""
METODOS DE TUPLAS
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

thistuple = ("apple", "banana", "cherry")
print("la tupla es:")
print(thistuple)
print("")
print("El segundo miembro de la tupla es:")
print(thistuple[1])
#La siguiente linea no tiene sentido porque las tuplas son inmutables (no da error pero no se modifica la tupla)
thistuple[1] = "blackcurrant"
print("Recorremos la tupla")
for x in thistuple:
  print(x)
print("Comprobamos que existe 'apple' en la tupla")
if "apple" in thistuple:
  print("si, 'apple' está en la tupla")
print("La longitud de la tupla es:")
print(len(thistuple))
print("Borramos la tupla (Se espera error por intentar mostrar el contenido de la tupla despues de borrarla)")
del thistuple
print(thistuple)
print("Creamos la tupla con el constructor tuple()")
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)