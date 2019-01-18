#If...else
"""
Python soporta las condiciones lógicas habituales de las matemáticas:
    Igual: a == b
    No Igual: ! A = b
    Menos de: a <b
    Menos de o igual a: a <= b
    Mayor que: a> b
    Mayor que o igual a: a> = b

"""
print("Ver codigo para más información")
a = 33
b = 200
if b > a:
  print("b es mayor que a")
#elif si la condicion anterior no es cierta, trata esta:
a = 33
b = 33
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")
#else si ninguna de las anteriores es cierta entonces: se puede usar sin elif
a = 200
b = 33
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")
else:
  print("a es mayor que b")
#si solo hay una instruccion que ejecutar se puede poner en la misma linea que la condicional
if a > b: print("a es mayor que b")
#igualmente para el else
print("A") if a > b else print("B")
#condicion doble con operador logico and
c = 300
if a > b and c > a:
  print("Ambas condiciones son ciertas")
#condicion doble con operador logico or
if a > b or a > c:
  print("Por lo menos una de las condiciones es cierta")