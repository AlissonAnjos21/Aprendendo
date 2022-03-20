class File:
    def __init__(self, file, mode):
        print('Abrindo')
        self.file = open(file, mode)
    
    def __enter__(self):
        print('Entrando')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando')
        self.file.close()
        # Se for tratar alguma exceção ao fim do tratamento dar um return True

import os
diretorio = os.path.dirname(__file__)
nome = 'ex1.txt'
file = os.path.join(diretorio, nome)

with File(file, 'w+') as f:
    f.write('PRIMEIRA LINHA\n')
    f.write('SEGUNDA LINHA\n')
    f.write('TERCEIRA LINHA\n')
    