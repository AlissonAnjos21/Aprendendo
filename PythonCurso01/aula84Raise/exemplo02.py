# Criando as minhas exceções

def divisao(n1, n2):
    if n2 == 0:
        raise ValueError('O valor de n2 não pode ser 0.')
    return n1/n2

# Gera um erro novamente
# print(divisao(1, 0))

try:
    print(divisao(1, 0))
except ValueError as erro:
    print('Não tente dividir um número por zero')
    print('O erro foi: ', erro)
