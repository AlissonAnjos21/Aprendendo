# Produto - A ordem importa, os valores únicos SÃO repetidos

from itertools import product

frutas = ['Melão', 'Morango', 'Melancia', 'Mamão', 'Manga']

# Na função product deve se informar o que quer combinar junto com a quantidade que ele deverá repetir os casos idênticos.
for conjunto in product(frutas, repeat=2):
    # Percebe-se que neste caso ele repete o que já apareceu antes, e também mostra as combinações de casos idênticos.
    print(conjunto)
