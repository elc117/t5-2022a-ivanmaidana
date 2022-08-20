from Paciente import Paciente
from Setor import Setor
from Hospital import Hospital

if __name__ == '__main__':
    lista_pacientes_ontologia = []
    lista_pacientes_ortopedia = []
    lista_pacientes_cardivascular= []
    lista_setores = []
    paciente = Paciente("maria", 59, 41077600199, "A-", "ontologia")
    paciente1 = Paciente("mario", 67, 41077600100, "o+", "ontologia")
    paciente2 = Paciente("marinalva", 99, 41077600109, "o+", "ontologia")
    paciente3 = Paciente("jose", 69, 41077670180, "o-", "ortopedia")
    paciente4 = Paciente("joao", 19, 41077660108, "A+", "cardivascular")
    paciente5 = Paciente("paulo", 89, 41077650156, "o-", "cardivascular")

    lista_pacientes_ontologia.append(paciente)
    lista_pacientes_ontologia.append(paciente1)
    lista_pacientes_ontologia.append(paciente2)

    lista_pacientes_ortopedia.append(paciente3)

    lista_pacientes_cardivascular.append(paciente4)
    lista_pacientes_cardivascular.append(paciente5)

    ontologia = Setor("Ontologia", lista_pacientes_ontologia)
    ortopedia = Setor("Ortopedia", lista_pacientes_ortopedia)
    cardivascular = Setor("Cardivascular", lista_pacientes_cardivascular)

    lista_setores.append(ontologia)
    lista_setores.append(ortopedia)
    lista_setores.append(cardivascular)

    hospital_estadual = Hospital("HUSM", lista_setores)
    total = hospital_estadual.total_pacientes()
    print("Existem %d internados no hospital: %s" %(total, hospital_estadual.get_nome_hospital()))
