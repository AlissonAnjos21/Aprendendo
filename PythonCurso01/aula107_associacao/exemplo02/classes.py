class Agricultor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None


    @property
    def nome(self):
        return self.__nome


    @property
    def ferramenta(self):
        return self.__ferramenta


    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Enxada:
    def __init__(self, tipo):
        self.__tipo = tipo


    @property
    def tipo(self):
        return self.__tipo


    def arar(self):
        print('A enxada está arando o solo...')


class Trator:
    def arar(self):
        print('O trator está arando o solo...')

