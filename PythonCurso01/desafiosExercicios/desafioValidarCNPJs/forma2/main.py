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

from cnpj import pegar_cnpj, ser_cnpj, listar_cnpj, multiplicar, validar_cnpj

while True:
    cnpj_usuario = pegar_cnpj()
    invalido = ser_cnpj(cnpj_usuario)

    # Se for inválido, ele irá para o novo loop do while, ou seja, pedirá outro CNPJ
    if invalido:
        continue

    lista_cnpj_usuario = []
    parte_1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    parte_2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

    lista_cnpj_usuario = listar_cnpj(cnpj_usuario, lista_cnpj_usuario)

    lista_cnpj_usuario = multiplicar(lista_cnpj_usuario, parte_1)
    lista_cnpj_usuario = multiplicar(lista_cnpj_usuario, parte_2)

    validar_cnpj(lista_cnpj_usuario, cnpj_usuario)