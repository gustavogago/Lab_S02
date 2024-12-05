# curso_model.py

from database import conectar
from bson.objectid import ObjectId

db = conectar()
cursos_collection = db['cursos']

class CursoModel:
    def create_curso(self, nome_curso, descricao, creditos):
        curso_data = {
            'nome_curso': nome_curso,
            'descricao': descricao,
            'creditos': creditos,
            'estudantes_inscritos': []
        }
        result = cursos_collection.insert_one(curso_data)
        print(f"Curso {nome_curso} criado com ID {result.inserted_id}")
        return result.inserted_id

    def read_curso_by_id(self, id):
        curso = cursos_collection.find_one({'_id': ObjectId(id)})
        if curso:
            return curso
        else:
            print("Curso não encontrado.")
            return None

    def update_curso(self, id, nome_curso=None, descricao=None, creditos=None):
        update_fields = {}
        if nome_curso is not None:
            update_fields['nome_curso'] = nome_curso
        if descricao is not None:
            update_fields['descricao'] = descricao
        if creditos is not None:
            update_fields['creditos'] = creditos
        if update_fields:
            cursos_collection.update_one({'_id': ObjectId(id)}, {'$set': update_fields})
            print(f"Curso com ID {id} atualizado.")
        else:
            print("Nenhum campo para atualizar.")

    def delete_curso(self, id):
        cursos_collection.delete_one({'_id': ObjectId(id)})
        print(f"Curso com ID {id} deletado.")

    def list_cursos(self):
        cursos = cursos_collection.find()
        for curso in cursos:
            print(f"ID: {curso['_id']}, Nome do Curso: {curso['nome_curso']}, Créditos: {curso['creditos']}")
