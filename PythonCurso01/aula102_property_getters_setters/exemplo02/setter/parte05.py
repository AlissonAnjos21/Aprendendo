# Reforço setter:

class Comida:
    def __init__(self, categoria=None):
        # Agora ele está chamando o atributo setter categoria e passando para ele o valor da inicialização
        # Após isso, ele define que o "atributo fantasma (privado)" _categoria é o valor da inicialização
        self.categoria = categoria

    @property
    def categoria(self):
        # Estou retornando o valor do "atributo fantasma (privado)" _categoria, logo, o valor do método getter que se comporta como atributo (categoria) se torna este
        return self._categoria


    @categoria.setter
    def categoria(self, categoria):
        print('O SETTER FOI EXECUTADO COM SUCESSO!')
        self._categoria = categoria


c1 = Comida('Salgado')  # O SETTER FOI EXECUTADO COM SUCESSO!
