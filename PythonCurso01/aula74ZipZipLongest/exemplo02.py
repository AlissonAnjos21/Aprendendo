produto = ['Chocolate', 'Água', 'Sabão', 'Camisa', 'Barra de Ferro']
tipo = ['Comida', 'Bebida', 'Limpeza', 'Vestimenta']

tipo_produto = zip(tipo, produto)

# Vale lembrar que o funcão zip devolve um gerador, então após esgotados os seus valores não é possível recuperá-los normalmente. Então, se eu converter essa variável para lista, não é possível usar um for nela e vice-versa.
for valor in tipo_produto:
    print(valor)
