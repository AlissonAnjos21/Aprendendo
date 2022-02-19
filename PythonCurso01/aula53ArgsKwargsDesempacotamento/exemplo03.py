# Args com desempacotamento

def mostra_valores(*args):
    for valor in args:
        print(valor)


lista = [1, 2, 3, 4, 5]

mostra_valores(lista)  # Imprimo a lista toda como se ela fosse um ÚNICO parâmetro
mostra_valores(*lista)  # Desempacoto a lista e transformo CADA VALOR dela em um parâmetro
