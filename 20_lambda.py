#funciones Lambda python
#sintaxis lambda arguments : expression (puede recibir cualquier numero de argumentos separados por comas)
x = lambda a : a + 10
print(x(5))
y = lambda a, b : a * b
print(y(5, 6))
#Usado como funcion anonima dentro de otra función
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
print("Ver codigo")
