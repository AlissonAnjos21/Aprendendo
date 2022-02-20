# Problemas ao usar elementos mutáveis (como listas) como parâmetros de uma função

# Mutáveis: Listas, dicionários
# Imutáveis: Tuplas, strings, inteiros, floats, True, False, None

# Erro:
# Não deve ser feito, já que a lista é um valor mutável, ao usá-la toda vez que ela for chamada os valores anteriores se manterão:
def lista_incorreta(lista_recebida, lista_base=[]):
    lista_base.extend(lista_recebida)
    return lista_base

lista_01 = ['Vermelho', 'Preto', 'Azul']
lista_02 = ['Cinza', 'Verde', 'Amarelo']
lista_03 = ['Rosa', 'Violeta', 'Branco']

# Todas as listas recebem os valores'Vermelho', 'Preto', 'Azul', 'Cinza', 'Verde', 'Amarelo', 'Rosa', 'Violeta' e 'Branco'
# O erro só ocorre quando você não envia o parâmetro nomeado ("lista_base")
erro_01 = lista_incorreta(lista_01)  
erro_02 = lista_incorreta(lista_02)
erro_03 = lista_incorreta(lista_03)

print(erro_01)
print(erro_02)
print(erro_03)



# Correto:
# Para resolver, basta definir um elemento imutável como parâmetro base (None, por exemplo)

def lista_incorreta(lista_recebida, lista_base=None):
    if lista_base is None:
        lista_base = []

    lista_base.extend(lista_recebida)
    return lista_base


lista_01 = ['Vermelho', 'Preto', 'Azul']
lista_02 = ['Cinza', 'Verde', 'Amarelo']
lista_03 = ['Rosa', 'Violeta', 'Branco']

correta_01 = lista_incorreta(lista_01)
correta_02 = lista_incorreta(lista_02)
correta_03 = lista_incorreta(lista_03)

print(correta_01)
print(correta_02)
print(correta_03)
