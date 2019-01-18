#se debera ejecutar primero demo_mongodb_test para crear la bbdd
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()
print("Buscamos el primer documento de la colección")
print(x)

print("Ahora buscamos todos los documentos de la colección costumers")
for x in mycol.find():
  print(x)

print("Buscamos todos los documentos pero ahora sin ID")
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

print("Ahora vamos a buscar documentos con la dirección Park Lane 38")
myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x) 

print("Vamos a buscar todos los documentos que tengan un adress que comience por S o superior (alfabeticamente)")
myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

print("Vamos a buscar todos los documentos que tengan un adress que comience por S con REGEX")
myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
  
print("Mostrando resultados ordenados por nombre(alfabeticamente)")
mydoc = mycol.find().sort("name")
for x in mydoc:
  print(x)

#usando el segundo parametro del sort podemos indicar si ordenar ascendente o descendentemente
print("Ordenando alfabeticamente pero a la inversa")
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
  print(x)