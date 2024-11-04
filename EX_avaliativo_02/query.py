# query.py
from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]

# Questão 01

db = Database("neo4j://localhost:7687", "neo4j", "password")

# a
renzo_data = db.query("""
    MATCH (t:Teacher {name: 'Renzo'})
    RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
""")
print(renzo_data)

# b
teachers_with_m = db.query("""
    MATCH (t:Teacher)
    WHERE t.name STARTS WITH 'M'
    RETURN t.name AS name, t.cpf AS cpf
""")
print(teachers_with_m)

# c
cities = db.query("""
    MATCH (c:City)
    RETURN c.name AS name
""")
print(cities)

# d
schools_in_range = db.query("""
    MATCH (s:School)
    WHERE s.number >= 150 AND s.number <= 550
    RETURN s.name AS name, s.address AS address, s.number AS number
""")
print(schools_in_range)

# Questão 02 

# a
age_range = db.query("""
    MATCH (t:Teacher)
    RETURN max(t.ano_nasc) AS mais_jovem, min(t.ano_nasc) AS mais_velho
""")
print(age_range)

# b
avg_population = db.query("""
    MATCH (c:City)
    RETURN avg(c.population) AS media_populacao
""")
print(avg_population)

# c
city_with_cep = db.query("""
    MATCH (c:City {cep: '37540-000'})
    RETURN replace(c.name, 'a', 'A') AS nome_modificado
""")
print(city_with_cep)

# d
teacher_characters = db.query("""
    MATCH (t:Teacher)
    RETURN substring(t.name, 2, 1) AS char_terceira_letra
""")
print(teacher_characters)

db.close()
