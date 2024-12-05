# main.py

from estudante_cli import EstudanteCLI
from curso_cli import CursoCLI
from estudante_model import EstudanteModel
from curso_model import CursoModel
from database import conectar
from bson.objectid import ObjectId

db = conectar()
estudantes_collection = db['estudantes']
cursos_collection = db['cursos']

def matricular_estudante():
    print("\n--- Matrícula de Estudante em Curso ---")
    estudante_id = input("Enter the Estudante ID: ")
    estudante = estudantes_collection.find_one({'_id': ObjectId(estudante_id)})
    if not estudante:
        print("Estudante não encontrado.")
        return
    curso_id = input("Enter the Curso ID: ")
    curso = cursos_collection.find_one({'_id': ObjectId(curso_id)})
    if not curso:
        print("Curso não encontrado.")
        return

    # Atualizar listas de inscritos
    if curso_id not in estudante['cursos_inscritos']:
        estudante['cursos_inscritos'].append(curso_id)
        estudantes_collection.update_one(
            {'_id': ObjectId(estudante_id)},
            {'$set': {'cursos_inscritos': estudante['cursos_inscritos']}}
        )

    if estudante_id not in curso['estudantes_inscritos']:
        curso['estudantes_inscritos'].append(estudante_id)
        cursos_collection.update_one(
            {'_id': ObjectId(curso_id)},
            {'$set': {'estudantes_inscritos': curso['estudantes_inscritos']}}
        )

    print(f"Estudante {estudante['nome']} matriculado no curso {curso['nome_curso']}.")

def main_menu():
    while True:
        print("\n===== Sistema de Controle de Estudantes =====")
        print("1. Gerenciar Estudantes")
        print("2. Gerenciar Cursos")
        print("3. Matrícula")
        print("4. Sair")
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            estudante_cli = EstudanteCLI(EstudanteModel())
            estudante_cli.run()
        elif opcao == '2':
            curso_cli = CursoCLI(CursoModel())
            curso_cli.run()
        elif opcao == '3':
            matricular_estudante()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
