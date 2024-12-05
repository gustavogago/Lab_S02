# estudante_cli.py

from simple_cli import SimpleCLI
from estudante_model import EstudanteModel

class EstudanteCLI(SimpleCLI):
    def __init__(self, estudante_model):
        super().__init__()
        self.estudante_model = estudante_model
        self.add_command("create", self.create_estudante)
        self.add_command("read", self.read_estudante)
        self.add_command("update", self.update_estudante)
        self.add_command("delete", self.delete_estudante)
        self.add_command("list", self.list_estudantes)

    def create_estudante(self):
        nome = input("Enter the name: ")
        idade = int(input("Enter the age: "))
        matricula = input("Enter the matricula: ")
        self.estudante_model.create_estudante(nome, idade, matricula)

    def read_estudante(self):
        id = input("Enter the id: ")
        estudante = self.estudante_model.read_estudante_by_id(id)
        if estudante:
            print(f"Name: {estudante['nome']}")
            print(f"Age: {estudante['idade']}")
            print(f"Matricula: {estudante['matricula']}")
            print(f"Cursos Inscritos: {estudante['cursos_inscritos']}")

    def update_estudante(self):
        id = input("Enter the id: ")
        nome = input("Enter the new name (leave blank to keep current): ")
        idade_input = input("Enter the new age (leave blank to keep current): ")
        matricula = input("Enter the new matricula (leave blank to keep current): ")
        idade = int(idade_input) if idade_input else None
        nome = nome if nome else None
        matricula = matricula if matricula else None
        self.estudante_model.update_estudante(id, nome, idade, matricula)

    def delete_estudante(self):
        id = input("Enter the id: ")
        self.estudante_model.delete_estudante(id)
        
    def list_estudantes(self):
        self.estudante_model.list_estudantes()

    def run(self):
        print("Welcome to the Estudante CLI!")
        print("Available commands: create, read, update, delete, list, quit")
        super().run()
