#Archivo python
try:
  print(x)
except NameError:
  print("Variable x no está definida")
except:
  print("Ha ocurrido una excepcion")
  
try:
  print("Hola")
except:
  print("Something went wrong")
else:
  print("No ha ocurrido ningún error")
finally:
	print("Finalmente se acaba el try")