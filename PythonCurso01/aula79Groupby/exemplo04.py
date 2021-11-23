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

from itertools import groupby, tee

agrupamento = groupby(alunos, chave)

# Caso eu queira além da quantidade de itens em cada grupo, os itens em si.
# Para isso é necessário importar a função tee, com ela é possível gerar uma copia do objeto iterador, já que, por formas convencionais, não é possível ver a quantidade de itens e os itens em si, pois, o iterador vai até o seu fim e se esgota, sendo então necessário o uso de uma copia não esgotada desse iterador para concluir a operação.

for grupo, itens in agrupamento:
    print(f'O grupo é o: {grupo}')

    # Usando a função tee
    copia1, copia2 = tee(itens)

    quantidade = len(list(copia1))
    print(f'\tA quantidade de alunos nesse grupo é: {quantidade}')
    for item in copia2:
        print( f'\t{item["nome"]}')
