# Combinação - A ordem não importa, os valores únicos NÃO são repetidos

from itertools import combinations

frutas = ['Melão', 'Morango', 'Melancia', 'Mamão', 'Manga']

# Na função combinations deve se informar o que quer combinar junto com de quanto em quanto que se quer combinar.
for conjunto in combinations(frutas, 2):
    # Percebe-se que ele não repete em outra ordem o que já apareceu antes.
    print(conjunto)
