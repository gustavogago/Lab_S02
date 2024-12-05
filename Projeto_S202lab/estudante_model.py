# estudante_model.py

from database import conectar
from bson.objectid import ObjectId

db = conectar()
estudantes_collection = db['estudantes']

class EstudanteModel:
    def create_estudante(self, nome, idade, matricula):
        estudante_data = {
            'nome': nome,
            'idade': idade,
            'matricula': matricula,
            'cursos_inscritos': []
        }
        result = estudantes_collection.insert_one(estudante_data)
        print(f"Estudante {nome} criado com ID {result.inserted_id}")
        return result.inserted_id

    def read_estudante_by_id(self, id):
        estudante = estudantes_collection.find_one({'_id': ObjectId(id)})
        if estudante:
            return estudante
        else:
            print("Estudante não encontrado.")
            return None

    def update_estudante(self, id, nome=None, idade=None, matricula=None):
        update_fields = {}
        if nome is not None:
            update_fields['nome'] = nome
        if idade is not None:
            update_fields['idade'] = idade
        if matricula is not None:
            update_fields['matricula'] = matricula
        if update_fields:
            estudantes_collection.update_one({'_id': ObjectId(id)}, {'$set': update_fields})
            print(f"Estudante com ID {id} atualizado.")
        else:
            print("Nenhum campo para atualizar.")

    def delete_estudante(self, id):
        estudantes_collection.delete_one({'_id': ObjectId(id)})
        print(f"Estudante com ID {id} deletado.")

    def list_estudantes(self):
        estudantes = estudantes_collection.find()
        for estudante in estudantes:
            print(f"ID: {estudante['_id']}, Nome: {estudante['nome']}, Matrícula: {estudante['matricula']}")
