import re


def numerificar(cnpj_usuario):
    # Substitui por '' (vazio) qualquer coisa que não estiver entre 0 e 9, no cnpj_usuario 
    return re.sub(r'[^0-9]', '', cnpj_usuario)


def forma_lista(cnpj_usuario, lista_cnpj):
    if len(cnpj_usuario) != 14:
        print('\nEste CNPJ não é válido!\n')
        return
    else:
        for v in range(len(cnpj_usuario) - 2):
            lista_cnpj.append(int(cnpj_usuario[v]))
        return lista_cnpj


