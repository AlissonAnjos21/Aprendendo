"""
No Python existem convenções onde os programadores entendem que podem ou não usar algo

Deixando uma classe "privada":
_NOMEATRIBUTO Simboliza que o atributo ou método não deve ser acessado ou modificado fora da classe

"""

class Carro:
    def __init__(self):
        # Perceba que a lista de carros começa com "_", isso demonstra que este atributo é "privado" e não deve ser acessado fora da classe
        self._lista_carros = {}


    def inserir_carro(self, id, nome):
        if 'carros' in self._lista_carros:
            self._lista_carros['carros'].update({id:nome})
        else:
            self._lista_carros['carros'] = {id:nome}


    def remover_carro(self, id):
        del self._lista_carros['carros'][id]
    

    def mostrar_carros(self):
        for id, nome in self._lista_carros['carros'].items():
            print(id, nome)


c1 = Carro()
c1.inserir_carro(1, 'Corsa')
c1.inserir_carro(2, 'Mustang')
c1.inserir_carro(3, 'Camaro')

# É uma convenção não acessar fora da classe nenhum método ou atributo que começe com "_"
# Mas mesmo que a lista de carros esteja "privada" ainda é possível acessá-la de fora da classe (embora não se deva fazer isso)
# Desta maneira:
c1._lista_carros = 'Quebrei a classe novamente 😜🤡'

print(c1._lista_carros)
