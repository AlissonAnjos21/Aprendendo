class Exemplo:
    def __new__(cls, *args, **kwargs):
        print('Eu sou o primeiro a ser executado :D')
        print('Eu sou executado antes mesmo do init')
        return object.__new__(cls)  # Equivale a: return super().__new__(cls)
    def __init__(self):
        print('\nEu sou o segundo a ser executado :(')
        print('Eu sou executado após o new ')

exemplo = Exemplo()
