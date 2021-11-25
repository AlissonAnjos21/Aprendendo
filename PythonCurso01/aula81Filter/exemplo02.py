from dados import produtos

maior_dez = filter(lambda x: x['valor'] > 60, produtos)

# Perceba que todo o dicionário foi filtrado, e não apenas o campo "valor".
for produto in maior_dez:
    print(produto)
