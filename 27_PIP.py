#GEstor de paquetes python
"""
en la ruta donde tengamos los scripts
-Para comprobar la version de PIP
>> pip --version

-PAra instalar el paquete camelcase
#Encuentra más paquetes en https://pypi.org/
>>pip install camaelcase

-Para desinstalar un paquete 
>> pip uninstall camelcase

-Listar paquetes instalados
>>pip list

"""
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt)) 