#Diccionarios python
#Un diccionario es una colección que es desordenada, cambiante e indexado. En Python diccionarios se escriben con llaves, y tienen claves y valoresUn diccionario es una colección que es desordenada, cambiante e indexado. En Python diccionarios se escriben con llaves, y tienen claves y valores
"""
METODOS

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing the a tuple for each key value pair
keys()	Returns a list contianing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print("Valor de la clave 'model'")
x = thisdict["model"]
print(x)
print("Valor de la clave model pero usando get()")
x = thisdict.get("model")
print(x)
print("Cambiamos el valor de la clave year")
thisdict["year"] = 2018
print(thisdict)
print("Claves en el diccionario (bucle)")
for x in thisdict:
  print(x) 
print("Valores en el diccionario")
for x in thisdict:
  print(thisdict[x])
print("Valores en el diccionario pero usando values()")
for x in thisdict.values():
  print(x)
print("Claves y valores del diccionario con bucle")
for x, y in thisdict.items():
  print(x, y)
print("Comprobamos si existe la clave 'model' en el diccionario")
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
print("Cantidad de pares clave-valor que existen en el diccionario")
print(len(thisdict))
print("Añadimos un nuevo par clave-valor")
thisdict["color"] = "red"
print(thisdict)
print("Borramos el elemento con clave 'model' del diccionario")
thisdict.pop("model")
print(thisdict)
print("Borramos el último elemento insertado")
thisdict.popitem()
print(thisdict)
print("Borramos la diccionario")
thisdict.clear()
print(thisdict)
print("Creamos el diccionario con el constructor dic()")
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)