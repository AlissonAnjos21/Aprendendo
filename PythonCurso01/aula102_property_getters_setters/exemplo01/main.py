# @property: Getters e Setters

class Carro:
    def __init__(self, modelo, preco):
        self.modelo = modelo
        self.preco = preco
    

    def promocao(self, desconto):
        self.preco = self.preco - (self.preco * desconto / 100)

    # Getter
    # Precisa ser decorado com @property
    # Precisa possuir o nome do atributo ao qual ele é referente
    # O que é retornado precisa, por convenção, ser o nome do atributo precedido por "_"
    @property
    def preco(self):
        return self._preco
