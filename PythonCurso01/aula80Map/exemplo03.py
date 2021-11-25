from dados import produtos

# Pego todo o dicionário, e dele quando referente a coluna "valor" eu multiplico os valores por 1.21 e depois arredondo o valor obtido até a segunda casa decimal. Por fim, eu retorno todo o dicionário.
def aumentador_de_valores(x):
    x['valor'] = round(x['valor'] * 1.21, 2)
    return x

# Note que desse modo eu consigo um dicionário com os nomes e os valores aumentados, caso fosse feito a partir de uma função lambda ele retornaria apenas um campo da função (Neste caso o capo idade).
valor_aumantado = map(aumentador_de_valores, produtos)

# Antes
for produto in produtos:
    print(produto)

print('##########################################')

# Depois
for valor in valor_aumantado:
    print(valor)
