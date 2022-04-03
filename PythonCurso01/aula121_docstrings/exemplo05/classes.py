"""
Documentação de classes

Tempor duis sint irure ad duis est eiusmod. Duis eiusmod eu cupidatat occaecat ea eu cupidatat commodo ullamco ad excepteur. Magna laboris sunt reprehenderit sit cupidatat pariatur exercitation id veniam nulla voluptate culpa non cillum. 
Veniam cupidatat ut mollit dolore. Elit enim elit anim officia minim esse proident ex in amet officia. Qui reprehenderit laborum officia enim occaecat eu mollit nisi et sunt magna. 
Dolore reprehenderit sunt irure tempor labore aute tempor reprehenderit fugiat sunt esse enim aute.
"""

class UmaClasse:
    """Documentação da classe

    Lembrar de começar sempre na primeira linha da classe, assim como nas funções
    """
    atributo_1 = 'atributo 1'
    atributo_2 = 'atributo 2'

    def __init__(self, numero):
        """Inicializando os dados
        
        :param numero: numero a ser recebido na criação
        :type numero: int or float
        """
        self.numero = numero
        self.mostra_numero(numero)
    
    @staticmethod
    def mostra_numero(numero):
        """Esse método exibe um número recebito somado a 10 na tela
        
        :param numero: É um número
        :type numero: int or float

        :return: O número recebido mais 10
        :rtype: int or float

        :raises TypeError: Se o texto não for int ou float
        """
        if not isinstance(numero, (int, float)):
            raise TypeError('O número precisa ser um int ou um float')
        return numero + 10
