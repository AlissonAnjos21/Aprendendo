# Problemas ao usar elementos mutáveis (como listas) como parâmetros de uma função

# Mutáveis: Listas, dicionários
# Imutáveis: Tuplas, strings, inteiros, floats, True, False, None

# Erro, não deve ser feito, já que a lista é um valor mutável, ao usá-la toda vez que ela for chamada os valores anteriores se manterão:
# def lista_incorreta(lista_recebida, lista_base=[]):
#     lista_base.extends(lista_recebida)
#     return lista_base

# lista_01 = ['Vermelho', 'Preto', 'Azul']
# lista_02 = ['Cinza', 'Verde', 'Amarelo']
# lista_03 = ['Rosa', 'Violeta', 'Branco']

# # O erro só ocorre quando você não envia o parâmetro nomeado ("lista_base")
# erro_01 = lista_incorreta(lista_01)
# erro_02 = lista_incorreta(lista_02)
# erro_03 = lista_incorreta(lista_03)

# print(erro_01)
# print(erro_02)
# print(erro_03)




#
