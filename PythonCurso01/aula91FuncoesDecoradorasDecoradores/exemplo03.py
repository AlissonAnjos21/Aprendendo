# Funções que recebem parâmetros

def chefe(funcao):
    def empregado(*args, **kwargs):
        funcao(*args, **kwargs)
        print('O que eu faço? Eu imprimo coisas, ora bolas')
    return empregado


@chefe
def imprime_coisas(mensagem):
    print(mensagem)


imprime_coisas('Fala tu, o que tu faz, meu consagrado?')
