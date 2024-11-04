from teacher_crud import TeacherCRUD
from query import Database

db = Database("neo4j://localhost:7687", "neo4j", "password")
teacher_crud = TeacherCRUD(db)


#Questao 03

# a
teacher_crud.create("Chris Lima", 1956, "189.052.396-66")

# b
teacher = teacher_crud.read("Chris Lima")
print(teacher)

# c
teacher_crud.update("Chris Lima", "162.052.777-77")

# d
teacher_updated = teacher_crud.read("Chris Lima")
print(teacher_updated)

db.close()
