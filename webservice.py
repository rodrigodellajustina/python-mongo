from flask import Flask
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
dbveiculos = client['veiculos']

app = Flask(__name__)

@app.route('/v1/consulta/<cPlaca>')
def getVeiculo(cPlaca):

    jBuscaVeiculo = {"placa":cPlaca}
    listaVeiculo = dbveiculos.veiculos.find(jBuscaVeiculo)

    for veiculo in listaVeiculo:
        jsonRetorno = {"placa" : veiculo['placa'] ,
                       "nomeveiculo" : veiculo['nomeveiculo'],
                       "marca" : veiculo['marca'],
                       "ano" : veiculo['ano'],
                       "proprietario" : veiculo['proprietario']
                       }

    jdumpRetorno = json.dumps(jsonRetorno)
    return jdumpRetorno

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4004")