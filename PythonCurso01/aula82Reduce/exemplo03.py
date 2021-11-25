from dados import pessoas
from functools import reduce

soma_idades = reduce(lambda ac, x: x['idade'] + ac, pessoas, 0)
media_idades = soma_idades / len(pessoas)

print(f'A soma das idades é: {soma_idades}\nA média das idades é: {media_idades}')
