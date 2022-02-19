# Mais detalhes sobre desempacotamento:

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]

# Juntando duas listas com desepacotamento
juncao = *lista_1, *lista_2

# Forma incorreta
juncao_incorreta = lista_1, lista_2

print(juncao)
print(juncao_incorreta)
