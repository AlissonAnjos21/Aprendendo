from dados import pessoas

def e_maior(x):
    if x['idade'] >= 18:
        return True
    else:
        return False

# Também é possível usar uma função comum, porém o recomendado é que ela retorne True ou False, caso contrário é uma boa prática usar a função map.
maior_idade = filter(e_maior, pessoas)

for idade in maior_idade:
    print(idade)
