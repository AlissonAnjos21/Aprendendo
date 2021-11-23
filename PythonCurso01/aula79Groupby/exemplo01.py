# Groupby - Agrupar dados a partir de uma chave

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

# Antes de tentar agrupar os dicionários, é necessário que o que você quer ordenar esteja na ordem (Neste caso as notas), caso contrário encontrará erros.
# Para isso, pode ser feito uso da função sort.
# Lembrando que a função sort precisa de uma chave para saber pelo que ela vai ordenar.
chave = lambda item: item['nota']
alunos.sort(key=chave)

for aluno in alunos:
    print(aluno)

# Com a lista ordenada, agora é só agrupá-la a partir de determinada chave (Neste caso, a mesma chave que foi usada na função sort, ou seja, a nota).
from itertools import groupby

agrupamento = groupby(alunos, chave)

# É possível ver que cada grupo de notas já está separado, porém, ainda não é possível ver os seus valores.
for grupo in agrupamento:
    print(grupo)
    