# Kwargs:

# Os kwargs são referentes ao parâmetros nomeados

def fala_chave_e_valor(**kwargs):
    # kwargs é um dicionário
    for k, v in kwargs.items():
        print(k, v)


def fala_chave(**kwargs):
    for k in kwargs.keys():
        print(k)


def fala_valor(**kwargs):
    for v in kwargs.values():
        print(v)

fala_chave_e_valor(nome='Jurandir', sobrenome='Carvalho')
fala_chave(nome='Wagner', sobrenome='Silva')
fala_valor(nome='Darci', sobrenome='Oliveira')
