from contextlib import contextmanager

@contextmanager
def operacao(file, mode):
    try:
        print('Abrindo')
        f = open(file, mode)
        yield f
    finally:
        print('Fechando')
        f.close()

import os
diretorio = os.path.dirname(__file__)
nome = 'ex2.txt'
file = os.path.join(diretorio, nome)

with operacao(file, 'w+') as f:
    f.write('ESCREVENDO UMA LINHA\n')
    f.write('ESCREVENDO DUAS LINHAS\n')
    f.write('ESCREVENDO TRÊS LINHAS\n')
