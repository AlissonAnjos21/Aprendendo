from dados import produtos
from functools import reduce

total_preco = reduce(lambda ac, x: x['valor'] + ac, produtos, 0)

# Caso eu queira saber a média.
media = total_preco / len(produtos)

print(f'O total dos preços é: {total_preco}\nA média dos preços é: {media}')
