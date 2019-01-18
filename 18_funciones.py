#funciones python
"""
Una función es un bloque de código que sólo se ejecuta cuando se le llama.

Puede pasar datos, conocidos como parámetros, en una función.

Una función puede devolver datos como resultado.

"""

def my_function():
  print("Hola desde una funcion")
my_function()
print("Usando llamada a funcion con parametro (3 llamadas)")
def saluda(nombre):
  print("Hola " + nombre)
saluda("Emil")
saluda("Tobias")
saluda("Linus")
print("LLamada a funcion con parametro con valor por defecto si no se le pasa en la llamada(Noruega)")
def de_donde(pais = "Noruega"):
  print("Soy de " + pais)
de_donde("Suiza")
de_donde("India")
de_donde()
de_donde("Brasil")
print("Funcion que devuelve valores con return")
def retorna(x):
  return 5 * x
print(retorna(3))
print(retorna(5))
print(retorna(9))
