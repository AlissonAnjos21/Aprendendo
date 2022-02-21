"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""

import re

while True:
    cnpj_usuario = input('Informe um CNPJ para ser validado: \n')
    cnpj_usuario = re.sub(r'[^0-9]', '', cnpj_usuario)

    parte_1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    parte_2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    lista_cnpj_usuario = []

    if len(cnpj_usuario) != 14 or cnpj_usuario.isnumeric == False:
        print('\nEsse não é um CNPJ válido!')
    else:
        for v in range(len(cnpj_usuario) - 2):
            lista_cnpj_usuario.append(int(cnpj_usuario[v]))


    lista_soma = []
    for v in range(len(lista_cnpj_usuario)):
        lista_soma.append(lista_cnpj_usuario[v] * parte_1[v])


    digito = 11 - (sum(lista_soma) % 11)

    if digito > 9:
        lista_cnpj_usuario.append(0)
        digito = 0
    else:
        lista_cnpj_usuario.append(digito)
        digito = 0

    lista_soma.clear()

    for v in range(len(lista_cnpj_usuario)):
        lista_soma.append(lista_cnpj_usuario[v] * parte_2[v])

    digito = 11 - (sum(lista_soma) % 11)

    if digito > 9:
        lista_cnpj_usuario.append(0)
        digito = 0
    else:
        lista_cnpj_usuario.append(digito)
        digito = 0

    cnpj_verificado = ''
    for v in lista_cnpj_usuario:
        cnpj_verificado += str(v)

    if cnpj_usuario == cnpj_verificado:
        print('Este CNPJ é válido!!!\n')
    else:
        print('Este CNPJ NÃO É válido!!!\n')
        
