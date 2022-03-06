"""
Outras linguagens de programação: 
Public, Private, Protected
-Public: Consegue acessar o atributo ou método dentro ou fora da classe
+Private: Consegue acessar o atributo ou método apenas dentro da classe
#Protected: Consegue acessar o atributo ou método apenas dentro da classe ou dentro das classes filhas da classe

No python, esses conceitos não existem exatamente desta maneira
O que existe mais são convenções onde os programadores entendem que podem ou não usar algo

_NOMEATRIBUTO Simboliza que o atributo ou método não deve ser acessado ou modificado fora da classe

___NOMEATRIBUTO Simboliza FORTEMENTE que o atributo ou método não deve ser acessado ou modificado fora da classe

Neste ultimo caso, o simbolismo é tamanho que para conseguir se acessar tal atributo ou método, é necessário usar: instancia._NOMECLASSE__nomeatributo/metodo
Ex: p1._Pessoa__nome
"""

class Carro:
    def __init__(self):
        self.lista_carros = {}


    def inserir_carro(self, id, nome):
        if 'carros' in self.lista_carros:
            self.lista_carros['carros'].update({id:nome})
        else:
            self.lista_carros['carros'] = {id:nome}


    def remover_carro(self, id):
        del self.lista_carros['carros'][id]
    

    def mostrar_carros(self):
        for id, nome in self.lista_carros['carros'].items():
            print(id, nome)


# As coisas funcionam, porém algo perigoso pode ocorrer (segue para o próximo exemplo)
c1 = Carro()
c1.inserir_carro(1, 'Corsa')
c1.inserir_carro(2, 'Mustang')
c1.inserir_carro(3, 'Camaro')

c1.remover_carro(1)
c1.mostrar_carros()
