from pymongo import MongoClient

# instalação do pymongo
# /Python/scripts
# pip install pymongo

client = MongoClient('localhost', 27017)
dbveiculos = client['veiculos']

def cadastraveiculo():
    placa        = input('Placa.........: ')
    nomeveiculo  = input('Nome Veiculo..: ')
    marca        = input('Marca.........: ')
    ano          = input('Ano...........: ')
    proprietario = input('Proprietario..: ')

    armazenarveiculo(placa, nomeveiculo, marca, ano, proprietario)

def armazenarveiculo(placa, nomeveiculo, marca, ano, proprietario):
    print('::Armazenando Veiculos::')
    print(placa)
    print(nomeveiculo)

    jveiculo = {"placa":placa,
                "nomeveiculo":nomeveiculo,
                "marca": marca,
                "ano": ano,
                "proprietario": proprietario}

    dbveiculos.veiculos.insert_one(jveiculo)

cadastraveiculo()