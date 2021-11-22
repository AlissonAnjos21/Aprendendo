# Usando a função Zip Longest:

from itertools import zip_longest

produto = ['Chocolate', 'Água', 'Sabão', 'Camisa', 'Barra de Ferro']
tipo = ['Comida', 'Bebida', 'Limpeza', 'Vestimenta']

# A função zip_longest por sua vez, preenche os valores que faltam ser preenchidos com "None" por padrão (este padrão pode ser alterado usando o fillvalue).

tipo_produto = zip_longest(tipo, produto, fillvalue='Outro')  # O que falta ser preenchido receberá por padrão o valor "Outro".

# Também é possível iterar sobre ele ou convertê-lo para lista, tupla, dicionário.
for valor in tipo_produto:
    print(valor)
