class Hospital:
    def __init__(self, nome, setores):
        self.nome = nome
        self.setores = setores

    def total_pacientes(self):
        conta_paciente=0
        lista_paciente =[]
        for setor in self.setores:
            lista_paciente = setor.get_pacientes()
            for paciente in lista_paciente:
                conta_paciente+=1
        return conta_paciente

    def get_nome_hospital(self):
        return self.nome