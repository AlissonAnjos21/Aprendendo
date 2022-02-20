import re


def numerificar(cnpj_usuario):
    # Substitui por '' (vazio) qualquer coisa que não estiver entre 0 e 9, no cnpj_usuario 
    return re.sub(r'[^0-9]', '', cnpj_usuario)

