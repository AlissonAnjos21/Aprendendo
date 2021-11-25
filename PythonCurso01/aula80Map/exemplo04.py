from dados import pessoas

nomes = map(lambda x: x['nome'], pessoas)
idades = map(lambda x: x['idade'], pessoas)
# Arredondei com o round para não aparecer nenhuma casa decimal.
novas_idades = map(lambda x: round(x['idade'] * 1.5), pessoas)

print(list(nomes))
print(list(idades))
print(list(novas_idades))

# Caso eu queira a lista inteira, ou seja, com os nomes e com a modificação das idades, eu precisarei criar uma função que resolva isso.
def aumentador_de_idades(x):
    x['idade'] = round(x['idade'] * 1.5)
    return x

pessoas_futuro = map(aumentador_de_idades, pessoas)

for pessoa in pessoas_futuro:
    print(pessoa)
