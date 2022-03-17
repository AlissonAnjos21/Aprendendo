class Exemplo:
    def __new__(cls, *args, **kwargs):
        # Criando um método de classe
        def sou_metodo(*args, **kwargs):
            print('Sou um método de classe :D')
        cls.sou_metodo = sou_metodo
        
        return object.__new__(cls)

    def __init__(self):
        print('Fui executado')

exemplo = Exemplo()
exemplo.sou_metodo()  # Sou um método de classe :D
    