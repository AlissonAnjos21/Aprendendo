class Exemplo:
    def __new__(cls, *args, **kwargs):
        # Criei um atributo de classe 
        cls.valor = 21
        return object.__new__(cls)
    
    def __init__(self):
        print('Fui executado')

exemplo = Exemplo()
print(exemplo.valor)  # 21
