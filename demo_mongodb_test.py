#Archivo python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
#Aunque no se especifique un campo id Mongo añade uno y asigna un id unico por documento
print("El ID del registro insertado es: ")
print(x.inserted_id) 


#Para comprobar si existe la BBDD
#En MongoDB no se crea la BBDD hasta que ésta no tiene contenido
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
#Para comprobar si existe la colección
#No se crea la colección hasta que la misma no tiene contenido 
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

#Prueba de varios inserts de golpe  
print("Ahora insertamos varios")
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
print("Los IDs de los registros insertados son:")
print(x.inserted_ids)