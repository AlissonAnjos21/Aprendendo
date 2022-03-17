class Exemplo01:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        pass

class Exemplo02:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        self.__dict__[key] = value

exemplo01 = Exemplo01()
exemplo01.nome = 'Carla'
# Erro: O método __setattr__ não foi utilizado
# print(exemplo01.nome)

exemplo02 = Exemplo02()
exemplo02.nome = 'Bruno'
# Agora com o __setattr__ devidamente configurado
print(exemplo02.nome)  # Bruno
