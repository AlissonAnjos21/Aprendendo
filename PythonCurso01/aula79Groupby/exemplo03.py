alunos = [
    {'nome': 'Jurandi', 'nota': 'B'},
    {'nome': 'Valdir', 'nota': 'C'},
    {'nome': 'Wagner', 'nota': 'A'},
    {'nome': 'Airlton', 'nota': 'D'},
    {'nome': 'Valdisney', 'nota': 'B'},
    {'nome': 'Cleber', 'nota': 'D'},
    {'nome': 'Cleiton', 'nota': 'C'},
    {'nome': 'Joilson', 'nota': 'C'},
    {'nome': 'Robson', 'nota': 'B'},
    {'nome': 'Ronaldo', 'nota': 'A'}
]
chave = lambda item: item['nota']
alunos.sort(key=chave)

from itertools import groupby

agrupamento = groupby(alunos, chave)

# Caso eu queira a quantidade de itens em cada grupo.
for grupo, itens in agrupamento:
    print(f'O grupo é o: {grupo}')

    quantidade = len(list(itens))
    print(f'\tA quantidade de alunos nesse grupo é: {quantidade}')
