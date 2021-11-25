from dados import pessoas

def e_maior(x):
    if x >= 18:
        return True
    else:
        return False

# também é possível usar uma função comum, porém o recomendado é que ela retorne True ou False, caso contrário é uma boa prática usar a função map.
maior_idade = filter(e_maior, pessoas)
