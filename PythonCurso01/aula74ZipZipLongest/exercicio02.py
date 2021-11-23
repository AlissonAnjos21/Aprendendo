# Crie um GERADOR que associe com a função zip as palavras "Batata" e "Batata"

gerador = ((x, y) for x, y in zip('Batata', 'Batata'))

from types import GeneratorType

print(isinstance(gerador, GeneratorType))  # True

# for valor in gerador:
#     print(valor)
