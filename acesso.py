from pymongo import MongoClient


# conexão com o  banco de dados
client = MongoClient('localhost', 27017)
# seleção do banco de dados
dbaulamongo = client['aulamongo']

#json de dados para envio no mongodb
jaula = {"laboratorio": "15",
         "aula" : "programação II"}

dbaulamongo.Aulas.insert_one(jaula)

listaAulas = dbaulamongo.Aulas.find({"laboratorio": "5"})

for lab in listaAulas:
    print(lab["_id"])