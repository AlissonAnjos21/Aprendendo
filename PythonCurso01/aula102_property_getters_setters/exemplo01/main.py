# @property: Getters e Setters

class Carro:
    def __init__(self, modelo, preco):
        self.modelo = modelo
        self.preco = preco
    
    
    # Continua funcionando normalmente mesmo após a definição do getter e do setter, não precisando mudar nenhum nome de atributo
    def promocao(self, desconto):
        self.preco = self.preco - (self.preco * desconto / 100)


    # Getter:
    # Precisa ser decorado com @property
    # Precisa possuir o nome do atributo ao qual ele é referente
    # O que é retornado precisa, por convenção, ser o nome do atributo precedido por "_"
    @property
    def preco(self):
        return self._preco


    # Setter:
    # Precisa ser decorado como (nome_do_atributo).setter
    # Precisa possuir o nome do atributo ao qual ele é referente
    # Precisa utilizar self.(nome_do_valor_retornado_pelo_getter)
    @preco.setter
    def preco(self, valor):
        # Métodos setters são úteis para tratar os valores antes de atribuí-los
        if isinstance(valor, str):
            # Desta maneira eu evito de receber uma string e/ou um possível "R$"
            valor = float(valor.replace('R$', ''))

        self._preco = valor

    
    @property
    def modelo(self):
        return self._modelo


    @modelo.setter
    def modelo(self, valor):
        # O lower deixa tudo minúsculo
        self._modelo = valor.lower()


c1 = Carro('Ferrari', 12100000)
print(c1.modelo)
print(c1.preco)

c1.promocao(10)  # 10%
print(c1.preco)

print('\n---------------------------\n')

c2 = Carro('Corsa', 'R$12000')
print(c2.modelo)
print(c2.preco)

c2.promocao(1)  # 1%
print(c2.preco)
