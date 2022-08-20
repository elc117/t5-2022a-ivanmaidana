class Paciente:
    def __init__(self, nome, idade, cpf, tipo_sanguineo, setor_onde_esta):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.tipoSanguineo = tipo_sanguineo
        self.setor_onde_esta = setor_onde_esta

    def pacinete(self):
        print(self.nome)
        print(self.idade)
        print(self.cpf)
        print(self.tipoSanguineo)
        print(self.setor_onde_esta)