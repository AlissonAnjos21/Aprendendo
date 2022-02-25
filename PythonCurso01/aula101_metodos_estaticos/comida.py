from random import randint

class Comida:

    def __init__(self, nome, validade):
        self.nome = nome
        self.validade = validade

    
    # Quando referente aos métodos estáticos, eles são métodos que NÃO recebem tanto o argumento da instância (self) quanto o argumento da classe (cls), ele atua de forma semelhante a uma função que está fora da classe, porém, por questões de organização, ele está inserido na própria classe
    # Para criá-lo é necessário decorá-lo com "@staticmethod"
    # Não é necessário passar argumentos para o mesmo, embora, é possível passar, caso necessário
    @staticmethod
    def criar_registro():
        # Como ele funciona de forma semelhante a uma função fora da classe, não é possível usar "self" nem "cls" dentro deste método
        rand = randint(10000, 99999)
        return rand
        
