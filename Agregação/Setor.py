class Setor:
    def __init__(self, nome, pacientes):
        self.nome = nome
        self.pacientes = pacientes

    def get_pacientes(self):
        return self.pacientes