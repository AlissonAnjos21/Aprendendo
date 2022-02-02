# Criando o módulo de funções
def seleciona_par(lista):
    return [x for x in lista if x % 2 == 0]


def seleciona_impar(lista):
    return [x for x in lista if x % 2 != 0]


def dobro(lista):
    return [x*2 for x in lista]


def metade(lista):
    return [x/2 for x in lista]
