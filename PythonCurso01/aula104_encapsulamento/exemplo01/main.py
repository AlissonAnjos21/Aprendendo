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

        
