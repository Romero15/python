#Listas python
"""
Hay cuatro tipos de datos recogida en el lenguaje de programación Python:

    Lista es una colección que es ordenado y cambiante. Permite a los miembros duplicados. se definen con [ ]
    Tupla es una colección que es ordenado e inmutable. Permite a los miembros duplicados. se definen con ( )
    Set es una colección que es desordenada y no indexados. No hay miembros duplicados.
    Diccionario es una colección que es desordenada, cambiante e indexado. No hay miembros duplicados.
	
METODOS para LISTAS
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""
thislist = ["apple", "banana", "cherry"]
print("Lista completa")
print("______________")
print(thislist) # salida >> ['apple', 'banana', 'cherry']
print("Segundo elemento de la lista")
print("____________________________")
print(thislist[1]) #salida >> banana
print("Cambia el segundo elemento de la lista")
print("______________________________________")
thislist[1] = "blackcurrant"
print(thislist)
print("Recorriendo los elementos de la lista")
print("_____________________________________")
for x in thislist:
  print(x) 
print("Comprobando si 'apple' existe en la lista")
print("_________________________________________")
if "apple" in thislist:
  print("Si, 'apple' existe en la lista")
print("Cantidad de elementos que contiene la lista")
print("___________________________________________")
print(len(thislist))
print("Añadimos el elemento 'orange' a la lista")
print("___________________________________________")
thislist.append("orange")
print(thislist)
print("Quitamos el elmento 'orange'")
print("___________________________________________")
thislist.remove("orange")
print(thislist)
print("Añadimos el elemento 'orange' a la lista en segunda posicion")
print("____________________________________________________________")
thislist.insert(1, "orange")
print(thislist)
print("Borramos el ultimo elemento de la lista")
print("_______________________________________")
thislist.pop()
print(thislist)
print("Borramos el elemento de indice expecificado de la lista (en este caso el primero)")
print("_________________________________________________________________________________")
del thislist[0] #del puede eliminar por completo la lista si solo se ejecuta del thislist
print(thislist)
print("Vaciamos la lista")
print("_________________")
thislist.clear()
print(thislist)
print("Creamos de nuevo la lista utilizando el constructor list()")
print("_________________________________________________________________________________")
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)