#Los literales de cadena en Python están delimitadas por comillas simples o comillas dobles (indiferenteme)
a = "Hello, World!"
print(a[0]) #Imprime 'H'
print(a[2:5]) #imprime de la posicion 2 a la 5 (no incluido)
b = " Hello, World! "
print(b.strip()) # elimina espacios de la cadena al principio y al final, retorna "Hello, World!" 
print(len(a)) # retorna la longitud de la cadena
print(a.lower()) # devuelve la cadena en minusculas
print(a.upper()) #devuelve la cadena en mayusculas
print(a.replace("H", "J")) #sustituye devuelve 'Jello, World!'
print(a.split(",")) #divide la cadena en subcadenas si encuntra instancias del saparador pasado como parametro  devuelve ['Hello', ' World!'] 
