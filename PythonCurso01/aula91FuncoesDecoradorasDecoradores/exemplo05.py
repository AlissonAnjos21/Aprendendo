# Um exemplo mais prático

from time import time

def chefe(funcao):
    def empregado(*args, **kwargs):
        comeco = time()
        resultado = funcao(*args, **kwargs)
        fim = time()
        demora = (fim - comeco) * 1000
        print(f'Ao todo, a função {funcao.__name__} demorou {demora:.3f} milisegundos')
        return resultado
    return empregado


@chefe
def contador(fim):
    for i in range(fim):
        print(f'Contentei até {i+1}')


contador(21)
