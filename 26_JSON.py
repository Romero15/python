#Archivo python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("JSON convertido a Diccionario de Python y sacamos el vamor de 'edad'")
print(y["age"])


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print("Convertir un objeto Python que contienen todos los tipos legales")
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print("Usar identacion para facilitar la lectura de los datos (indent)")
print(json.dumps(x, indent=4))
print("usar . y espacio para separar objetos , and a space, a = and a space to separate keys from their values")
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print("Ordenamos el resultado alfabeticamente (las claves)")
print(json.dumps(x, indent=4, sort_keys=True))

