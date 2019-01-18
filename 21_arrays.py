#Arrays python
#Los arrays se usan para almacenar varios valores en una unica variable
"""
Metodos para arrays
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
cars = ["Ford", "Volvo", "BMW"]
print("El array cars contiene:")
print(cars)
print("El primer elemento del arrays contiene:")
x = cars[0]
print(x)
print("Modificamos el primer elemento del array por Toyota")
cars[0]="Toyota"
print(cars)
print("Tamaño del array")
print(len(cars))
print("Recorremos el array printando todos los miembros")
for x in cars:
  print(x)
print("Añadimos un nuevo elemento al array (Honda)")
cars.append("Honda")
print(cars)
print("Borramos el segundo elemento de la lista")
#Tambien podemos borrar con .remove("Volvo")  Si  hay mas de un "Volvo" solo borra la primera ocurrencia.
cars.pop(1)
print(cars)