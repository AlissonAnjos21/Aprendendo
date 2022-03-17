class Exemplo01:
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        print('Fui inicializado')

class Exemplo02:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)  # Equivale a: return object.__new__(cls)

    def __init__(self):
        print('Fui inicializado')

exemplo01 = Exemplo01()  # ""
exemplo02 = Exemplo02()  # "Fui inicializado"
