# Permutação - A ordem importa, os valores únicos NÃO são repetidos

from itertools import permutations

frutas = ['Melão', 'Morango', 'Melancia', 'Mamão', 'Manga']

# Na função permutations deve se informar o que quer combinar junto com de quanto em quanto que se quer combinar.
for conjunto in permutations(frutas, 2):
    # Percebe-se que neste caso ele repete o que já apareceu antes, só que agora em outra ordem.
    print(conjunto)
