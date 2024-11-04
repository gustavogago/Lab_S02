class TeacherCRUD:
    def __init__(self, db):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = """
            CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        self.db.query(query, parameters={"name": name, "ano_nasc": ano_nasc, "cpf": cpf})

    def read(self, name):
        query = """
            MATCH (t:Teacher {name: $name})
            RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        result = self.db.query(query, parameters={"name": name})
        return result[0] if result else None

    def update(self, name, newCpf):
        query = """
            MATCH (t:Teacher {name: $name})
            SET t.cpf = $newCpf
        """
        self.db.query(query, parameters={"name": name, "newCpf": newCpf})

    def delete(self, name):
        query = """
            MATCH (t:Teacher {name: $name})
            DELETE t
        """
        self.db.query(query, parameters={"name": name})
