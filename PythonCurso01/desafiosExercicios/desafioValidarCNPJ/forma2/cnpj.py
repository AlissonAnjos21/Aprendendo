import re

def pegar_cnpj():
    cnpj_usuario = input('\nInforme um CNPJ para ser validado: \n')
    cnpj_usuario = re.sub(r'[^0-9]', '', cnpj_usuario)
    return cnpj_usuario


def ser_cnpj(cnpj_usuario):
    if cnpj_usuario == '':
        print('\nIsso NÃO é um CNPJ!!!\n')
        return True
    else:
        repeticao = cnpj_usuario[0] * len(cnpj_usuario)
        if cnpj_usuario == repeticao or len(cnpj_usuario) != 14:
            print('\nIsso NÃO é um CNPJ!!!\n')
            return True
        else:
            return False


def listar_cnpj(cnpj_usuario, lista_cnpj_usuario):
    for v in range(len(cnpj_usuario) - 2):
        lista_cnpj_usuario.append(int(cnpj_usuario[v]))
    return lista_cnpj_usuario


def multiplicar(lista_cnpj_usuario, parte):
    lista_soma = []
    for v in range(len(lista_cnpj_usuario)):
        lista_soma.append(lista_cnpj_usuario[v] * parte[v])
    digito = 11 - (sum(lista_soma) % 11)
    if digito > 9:
        lista_cnpj_usuario.append(0)
    else:
        lista_cnpj_usuario.append(digito)
    return lista_cnpj_usuario


def validar_cnpj(lista_cnpj_usuario, cnpj_usuario):
    cnpj_validado = ''
    for v in lista_cnpj_usuario:
        cnpj_validado += str(v)
    if cnpj_usuario == cnpj_validado:
        print('\nEste CNPJ é válido!!!\n')
    else:
        print('\nEste CNPJ NÃO É válido!!!\n')
    
