"""
Some o preço de todos os itens do carrinho
"""

carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 4', 50))

total = sum([float(y) for x, y in carrinho])
print(total)
