from flask import Flask
import json
from flask import request
from pymongo import MongoClient

app = Flask(__name__)
# conecta ao host
clientMongo = MongoClient('localhost', 27017)
# seta o banco de dados
dbunisep  = clientMongo['unisep']

@app.route('/aluno/<ra>', methods=['GET'])
def getAluno(ra):
    ira = int(ra)
    parametro = {"ra" : ira}
    listAluno = dbunisep.alunos.find(parametro)

    for aluno in listAluno:
        jsonAluno = {"ra" : aluno['ra'],
                     "nome" : aluno['nome'],
                     "cidade" : aluno['cidade']
                     }

    jdumpAluno = json.dumps(jsonAluno)

    return jdumpAluno

@app.route('/aluno/salvar', methods=['POST'])
def setAluno():
    # capturar o json
    jsonaluno   = request.json
    nomealuno   = jsonaluno['nome']
    ra          = jsonaluno['ra']
    cidadealuno = jsonaluno['cidade']
    cursoaluno  = jsonaluno['curso']

    # gravar no mongodb
    jsavealuno = {
        "nome" : nomealuno,
        "ra" : ra,
        "cidade" : cidadealuno,
        "curso" : cursoaluno
    }

    dbunisep.alunos.insert_one(jsavealuno)

    return {"Aluno" : "Salvo"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4001")