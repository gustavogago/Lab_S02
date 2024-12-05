# curso_cli.py

from simple_cli import SimpleCLI
from curso_model import CursoModel

class CursoCLI(SimpleCLI):
    def __init__(self, curso_model):
        super().__init__()
        self.curso_model = curso_model
        self.add_command("create", self.create_curso)
        self.add_command("read", self.read_curso)
        self.add_command("update", self.update_curso)
        self.add_command("delete", self.delete_curso)
        self.add_command("list", self.list_cursos)

    def create_curso(self):
        nome_curso = input("Enter the course name: ")
        descricao = input("Enter the description: ")
        creditos = int(input("Enter the credits: "))
        self.curso_model.create_curso(nome_curso, descricao, creditos)

    def read_curso(self):
        id = input("Enter the id: ")
        curso = self.curso_model.read_curso_by_id(id)
        if curso:
            print(f"Course Name: {curso['nome_curso']}")
            print(f"Description: {curso['descricao']}")
            print(f"Credits: {curso['creditos']}")
            print(f"Enrolled Students: {curso['estudantes_inscritos']}")

    def update_curso(self):
        id = input("Enter the id: ")
        nome_curso = input("Enter the new course name (leave blank to keep current): ")
        descricao = input("Enter the new description (leave blank to keep current): ")
        creditos_input = input("Enter the new credits (leave blank to keep current): ")
        creditos = int(creditos_input) if creditos_input else None
        nome_curso = nome_curso if nome_curso else None
        descricao = descricao if descricao else None
        self.curso_model.update_curso(id, nome_curso, descricao, creditos)

    def delete_curso(self):
        id = input("Enter the id: ")
        self.curso_model.delete_curso(id)
        
    def list_cursos(self):
        self.curso_model.list_cursos()

    def run(self):
        print("Welcome to the Curso CLI!")
        print("Available commands: create, read, update, delete, list, quit")
        super().run()
