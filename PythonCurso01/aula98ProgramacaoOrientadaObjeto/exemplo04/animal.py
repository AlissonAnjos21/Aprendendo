class Animal:
    def __init__(self, nome, idade, dormindo=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.dormindo = dormindo
        self.comendo = comendo

    def comer(self, comida):
        print(f'O animal {self.nome} está comento {comida}.')
        self.comendo = True
