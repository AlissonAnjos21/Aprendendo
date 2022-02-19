# Capturando um determinado elemento kwargs

def fala_nome_e_sobrenome(**kwargs):
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    print(sobrenome, nome)


fala_nome_e_sobrenome(nome='Seiya', sobrenome='Ryuuguuin')
