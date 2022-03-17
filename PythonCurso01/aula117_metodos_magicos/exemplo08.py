class Exemplo:
    def __init__(self):
        pass

    # Não é muito recomendável usar este método, pois a documentação do Python informa que ele nem sempre é chamado
    def __del__(self):
        print('Executo sempre que o Garbage Collector do Python é chamado, ou seja, no fim da execução')

exemplo = Exemplo()
