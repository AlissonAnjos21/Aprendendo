from dados import pessoas
from functools import reduce

soma_idades = reduce(lambda ac, x: x['idade'] + ac, pessoas, 0)
media_idades = soma_idades / len(soma_idades)
