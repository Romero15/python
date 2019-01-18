#Clases python
#Todo en Python es un objeto con sus propiedades y metodos
#Una clase es un constructor de objetos.
class MyClass:
  x = 5
p1 = MyClass()
#imprime el valor de x
print(p1.x)
#Todas las clases tienen una función llamada __init __ (), que siempre se ejecuta cuando se inicia la clase.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()

p1.age = 40
print("Ahora la edad de "+p1.name+" es: "+str(p1.age))

"""
Eliminar la propiedad del objeto edad p1:
del p1.age 

Eliminar el objeto p1:
del p1 


"""
