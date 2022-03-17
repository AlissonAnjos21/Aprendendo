class Exemplo:
    def __init__(self):
        pass

    # É chamado sempre que tentam usar como uma str o objeto instanciado
    def __str__(self):
        return 'Estão me usando como uma str'

exemplo = Exemplo()
print(exemplo)
