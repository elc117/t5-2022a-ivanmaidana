from Carro import Carro
from Motocicleta import Motocicleta


def imprime_carro(lista_carro):
    for carro in lista_carro:
        print("Nome: %s" %(carro.nome))
        print("Tipo: %s" %(carro.tipo))
        print("Marca: %s" %(carro.marca))
        print("Ano: %d" %(carro.ano))
        print("Quantas Portas: %d" %(carro.quantas_portas))
        print()

def imprime_moto(lista_moto):
    for moto in lista_moto:
        print("Nome: %s" % (moto.nome))
        print("Tipo: %s" % (moto.tipo))
        print("Marca: %s" % (moto.marca))
        print("Modelo: %s" % (moto.modelo))
        print("Ano: %d" % (moto.ano))
        print("Cilindradas: %d" % (moto.cilindrada))
        print()


if __name__ == '__main__':
    lista_carros = []
    lista_motos = []
    celta = Carro("celta", "carro", "chevrolet", "ret", 2004, 2)
    gol = Carro("gol", "carro", "volkswagen", "normal", 2016, 4)
    opala = Carro("opala", "carro", "chevrolet", "seda", 1989, 4)
    ybr = Motocicleta("ybr", "motocicleta", "Yamaha", "stret", 2012, 220)
    hornet = Motocicleta("hornet", "motocicleta", "Honda", "esportiva", 2012, 600)

    lista_carros.append(celta)
    lista_carros.append(gol)
    lista_carros.append(opala)

    lista_motos.append(ybr)
    lista_motos.append(hornet)

    imprime_carro(lista_carros)
    imprime_moto(lista_motos)
