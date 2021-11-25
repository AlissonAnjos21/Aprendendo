from dados import produtos

valores = map(lambda x: x['valor'], produtos)

# De todos os dicionários ele pegou apenas os valores dos produtos.
for valor in valores:
    print(valor)
