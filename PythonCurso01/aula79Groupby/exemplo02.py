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

# Agora é possível ver o grupo e o que está dentro dele.
for grupo, itens in agrupamento:
    print(f'O grupo é o: {grupo}')
    for item in itens:
        print(f'\t{item}')
