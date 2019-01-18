#Archivo python
print("Recorremos una lista con for")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print("Recorremos los caracteres de un string (banana)")
for x in "banana":
  print(x)
print("Salimos del bucle cuando x es banana")
for x in fruits:
  print(x)
  if x == "banana":
    break
print("Saltamos a la siguiente iteracion sin completar la actual con continue")
for x in fruits:
  if x == "banana":
    continue
  print(x)
print("Numero de iteraciones fijo (6) con range()")
#range(2,30,3) el primer parametro es en que iteracion empieza la ejecucion, el segundo hasta donde y el tercer parametro es el incremento (por defecto 1)
for x in range(6):
  print(x)
print("Condicion que se ejecuta al acabar el bucle (else)")
for x in range(6):
  print(x)
else:
  print("Acabe el bucle!")
print("Ahora bucles anidados")
adj = ["red", "big", "tasty"]
for x in adj:
  for y in fruits:
    print(x, y)
	