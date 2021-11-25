from dados import pessoas

def aumentador_de_idades_2(x):
    # Ao invés de incrimentar na própria coluna idade, eu estou criando uma nova coluna e arredondando os seus valores, após isso retornarei todo o dicionário.
    x['futura_idade'] = round(x['idade'] * 1.5)
    return x

pessoas_aumento = map(aumentador_de_idades_2, pessoas)

for pessoa in pessoas_aumento:
    print(pessoa)
