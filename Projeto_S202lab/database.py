from pymongo import MongoClient

def conectar():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['sistema_estudantes']
    return db
