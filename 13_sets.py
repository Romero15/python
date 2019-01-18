#sets python
"""
Un (set) conjunto es una colección que es desordenada y no indexados. En Python conjuntos se escriben con llaves
Una vez se crea un set no se pueden modificar sus elementos, pero si añadir nuevos.

METODOS
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others

"""
print("Creamos un conjunto")
thisset = {"apple", "banana", "cherry"}
print(thisset)
print("No se puede acceder a los miembros por inidce pero si recorrerlos con un for")
for x in thisset:
  print(x)
print("Comprueba si el elemento 'banana' existe en el set")
print("banana" in thisset)
print("Añadimos un nuevo elemento")
thisset.add("orange")
print(thisset)
print("Añadimos varios elementos de golpe a un set")
thisset.update(["mango", "grapes"])
print(thisset)
print("la longitud del set es:")
print(len(thisset))
print("Eliminamos 'bananana' de la lista, si no existiera devuelve error")
thisset.remove("banana")
print(thisset)
print("Intentamos eliminar de nuevo banana con discard() por lo que no devuelve error si no existe")
thisset.discard("banana")
print(thisset) 
print("Borramos el ultimo elemento con pop(), como los set son desordenados mostramos el elemento eleminado")
x = thisset.pop()
print("Borrado: " + x)
print("Ahora el set es; " + thisset)
print("Vaciamos el set")
thisset.clear()
print(thisset)
print("Creamos el set con el constructor")
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 