from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, nome, tipo, marca, modelo, ano, quantas_portas):
        super().__init__(nome, tipo, marca, modelo, ano)
        self.quantas_portas = quantas_portas

