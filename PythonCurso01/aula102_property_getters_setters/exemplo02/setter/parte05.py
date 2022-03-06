# Reforço setter:

# Obs: Chamo o _categoria de atributo fantasma pois o mesmo não é inicializado no método __init__, então o mesmo se torna oculto, porém ele é na verdade um atributo "privado"

class Comida:
    def __init__(self, categoria=None):
        # Agora ele está chamando o atributo setter categoria e passando para ele o valor da inicialização
        # Após isso, ele define que o "atributo fantasma (privado)" _categoria é o valor da inicialização
        self.categoria = categoria

    @property
    def categoria(self):
        # Estou retornando o valor do "atributo fantasma (privado)" _categoria, logo, o valor do método getter categoria (que se comporta como atributo) se torna o mesmo do _categoria
        return self._categoria


    @categoria.setter
    def categoria(self, categoria):
        print('O SETTER FOI EXECUTADO COM SUCESSO!')
        self._categoria = categoria


c1 = Comida('Salgado')  # O SETTER FOI EXECUTADO COM SUCESSO!
