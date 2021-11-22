# Usando a função zip:

produto = ['Chocolate', 'Água', 'Sabão', 'Camisa', 'Barra de Ferro']
tipo = ['Comida', 'Bebida', 'Limpeza', 'Vestimenta']

# É visível que a função zip associa os itens duas ou mais listas.
# Vale ressaltar que esta função vai até o ultimo item da menor lista, sendo assim, os outros valores não são incluidos.
tipo_produto = zip(tipo, produto)

# Esta função devolve um gerador, mas ainda assim é possível convertê-lo para uma lista, dicionário ou tupla .
print(list(tipo_produto))

# Também é possível iterar sobre ele.
# for valor in tipo_produto:
#     print(valor)
