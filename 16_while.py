#while python
print("Imprime el valor de 'i' siempre y cuando sea menor que 6, empezando por 1")
i = 1
while i < 6:
  print(i)
  i += 1
print("El mismo bucle pero con un break cuando el valor alcanza 3, el bucle se para aunque la condicion inicial sea cierta")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("El mismo bucle pero al alcanzar el valor 3 saltamos a la siguiente ejecucion sin acabar esta con continue")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
