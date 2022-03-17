class Exemplo:
    def __init__(self):
        pass

    def __del__(self):
        print('Executo sempre que o Garbage Collector do Python é chamado, ou seja, no fim da execução')

exemplo = Exemplo()
