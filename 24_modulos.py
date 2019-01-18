#Modulos python
#Cuando se utiliza una función de un módulo, utilice la sintaxis: module_name.function_name

import mymodule
mymodule.greeting("Jonathan")
#usar un alias de un modulo (ponerle otro nombre al modulo)
import mymodule as mx
a = mx.person1["age"]
print(a)
#Hay varios módulos incorporados en Python, que se pueden importar en cualquier momento
import platform
x = platform.system()
#Mostrará "Windows"
print(x) 
#La importación sólo el diccionario person1 del módulo
from mymodule import person1
print (person1["name"])