import random
import re


def numerificar(cnpj):
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    return cnpj


def listar_cnpj(cnpj, lista_cnpj):
    for v in range(len(cnpj)):
        lista_cnpj.append(int(cnpj[v]))
    return lista_cnpj


def multiplicar(lista_cnpj, parte):
    lista_soma = []
    for v in range(len(lista_cnpj)):
        lista_soma.append(lista_cnpj[v] * parte[v])
    digito = 11 - (sum(lista_soma) % 11)
    if digito > 9:
        lista_cnpj.append(0)
    else:
        lista_cnpj.append(digito)
    return lista_cnpj


def formatar(lista_cnpj):
    cnpj = ''
    for v in lista_cnpj:
        cnpj += str(v)
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}' 


def gerar_cnpj():
    parte_1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    parte_2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    lista_cnpj = []
   
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    concatenacao = f'{primeiro_digito}{segundo_digito}.{segundo_bloco}.{terceiro_bloco}/{quarto_bloco}'

    numeros_cnpj = numerificar(concatenacao)

    lista_cnpj = listar_cnpj(numeros_cnpj, lista_cnpj)

    lista_cnpj = multiplicar(lista_cnpj, parte_1)
    lista_cnpj = multiplicar(lista_cnpj, parte_2)

    cnpj = formatar(lista_cnpj)
    return cnpj

