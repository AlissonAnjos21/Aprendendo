from itertools import count

# Gera valores de 0 à diante.
indice = count()

produto = ['Chocolate', 'Água', 'Sabão', 'Camisa', 'Barra de Ferro']
tipo = ['Comida', 'Bebida', 'Limpeza', 'Vestimenta']

# A função zip/zip_longest, como mencionado antes, não se limita a dois valores.
indice_tipo_produto = zip(indice, tipo, produto)

# Também é possível desempacotar os valores obtidos
for valor1, valor2, valor3 in indice_tipo_produto:
    print(valor1, valor2, valor3)
