"""
___NOMEATRIBUTO Simboliza FORTEMENTE que o atributo ou método não deve ser acessado ou modificado fora da classe

Neste caso, o simbolismo é tamanho que para conseguir se acessar tal atributo ou método, é necessário usar: instancia._NOMECLASSE__nomeatributo/metodo

"""

class Carro:
    def __init__(self):
        # Perceba que a lista de carros começa com "_", isso demonstra que este atributo é "privado" e não deve ser acessado fora da classe
        self.__lista_carros = {}


    def inserir_carro(self, id, nome):
        if 'carros' in self.__lista_carros:
            self.__lista_carros['carros'].update({id:nome})
        else:
            self.__lista_carros['carros'] = {id:nome}


    def remover_carro(self, id):
        del self.__lista_carros['carros'][id]
    

    def mostrar_carros(self):
        for id, nome in self.__lista_carros.items():
            print(id, nome)


c1 = Carro()
c1.inserir_carro(1, 'Corsa')
c1.inserir_carro(2, 'Mustang')
c1.inserir_carro(3, 'Camaro')

c1.__lista_carros = "NÃOOOOOO, EU NÃO CONSIGO MAIS QUEBRAR A CLASSE 😭😭😭"  # Não faz literalmente NADA no código 😎, pois o atributo está fortemente privado

# O código abaixo exibe um erro, não é possível acessá-lo desta forma
# print(c1.__lista_carros)

# Para acessá-lo é necessário fazer da seguinte forma:
print(c1._Carro__lista_carros)  # Lembrando que NÃO É PARA ACESSÁ-LO DE FORA DA CLASSE
