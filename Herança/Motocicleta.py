from Veiculo import Veiculo

class Motocicleta(Veiculo):
    def __init__(self, nome, tipo, marca, modelo, ano, cilindrada):
        super().__init__(nome, tipo, marca, modelo, ano)
        self.cilindrada = cilindrada