#Iteradores python
"""
Un iterador es un objeto que contiene un número contable de valores.

Un iterador es un objeto que se pueden repetir en, lo que significa que se puede recorrer a través de todos los valores.

Técnicamente, en Python, un iterador es un objeto que implementa el protocolo iterador, que consisten en los métodos __iter__() y __next__().

"""
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

#Las cadenas tambien son iterables
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#crear un iterator que devuelve numeros a partir del 1 y cada secuencia se incrementa en 1
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 

#Iterator con StopIteration por si se usa el iterator en un bucle for (para establecer una condicion de parada)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)