# Reforço setter:

class Comida:
    def __init__(self, categoria=None):
        # Atribuirá à _categoria o valor da inicialização
        self._categoria = categoria

    @property
    def categoria(self):
        return self._categoria


    @categoria.setter
    def categoria(self, categoria):
        print('O SETTER FOI EXECUTADO COM SUCESSO!')
        self._categoria = categoria


c1 = Comida('Salgado')
print(c1.categoria)  # O setter não foi executado

print()
print('------------------------------')
print()

c2 = Comida()
c2.categoria = 'Doce'
print(c2.categoria)  # O SETTER FOI EXECUTADO COM SUCESSO!
