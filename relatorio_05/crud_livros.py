from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId

# Função para conectar ao MongoDB
def conectar_mongodb():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ping')  # Verifica a conexão
        print("Conectado ao MongoDB")
        return client
    except ConnectionFailure as e:
        print(f"Erro ao conectar no MongoDB: {e}")
        return None

# Classe para CRUD de Livros
class LivroModel:
    def __init__(self, database):
        self.db = database

    def create_livro(self, id, titulo, autor, ano, preco):
        try:
            res = self.db.Livros.insert_one({
                "_id": id,
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "preco": preco
            })
            print(f"Livro criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o livro: {e}")
            return None

    def read_livro_by_id(self, id):
        try:
            res = self.db.Livros.find_one({"_id": id})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o livro: {e}")
            return None

    def update_livro(self, id, titulo=None, autor=None, ano=None, preco=None):
        try:
            update_fields = {}
            if titulo:
                update_fields['titulo'] = titulo
            if autor:
                update_fields['autor'] = autor
            if ano:
                update_fields['ano'] = ano
            if preco:
                update_fields['preco'] = preco

            res = self.db.Livros.update_one({"_id": id}, {"$set": update_fields})
            print(f"Livro atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def delete_livro(self, id):
        try:
            res = self.db.Livros.delete_one({"_id": id})
            print(f"Livro deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None

# Menu para CRUD de Livros
def menu():
    client = conectar_mongodb()
    if not client:
        print("Falha ao conectar ao MongoDB. Saindo...")
        return

    db = client['biblioteca']
    livros_model = LivroModel(db)

    while True:
        print("\nMenu CRUD - Livros")
        print("1. Criar Livro")
        print("2. Ler Livro por ID")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            id = int(input("ID: "))
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            preco = float(input("Preço: "))
            livros_model.create_livro(id, titulo, autor, ano, preco)

        elif escolha == '2':
            id = int(input("ID do livro: "))
            livros_model.read_livro_by_id(id)

        elif escolha == '3':
            id = int(input("ID do livro: "))
            titulo = input("Novo Título (ou enter para ignorar): ")
            autor = input("Novo Autor (ou enter para ignorar): ")
            ano = input("Novo Ano (ou enter para ignorar): ")
            preco = input("Novo Preço (ou enter para ignorar): ")

            livros_model.update_livro(
                id,
                titulo if titulo else None,
                autor if autor else None,
                int(ano) if ano else None,
                float(preco) if preco else None
            )

        elif escolha == '4':
            id = int(input("ID do livro: "))
            livros_model.delete_livro(id)

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Escolha inválida! Tente novamente.")

# Chamar o menu
if __name__ == "__main__":
    menu()
