"""
As Dataclasses fornecem um módulo que disponibiliza um decorador e algumas funções para criar alguns métodos automaticamente e de forma mais enxuta/rápida.
As Dataclasses funcionam exatamente da mesma forma que as classes convencionais.
"""

from dataclasses import dataclass

@dataclass
class Carro:
    modelo: str
    quantidade_portas: int
    quantidade_passageiros: int

    def descrever(self):
        print(f'Olá, eu sou um método que descreve o carro criado.\nEste, por exemplo, é um {self.modelo} de {self.quantidade_portas} portas e com a capacidade de embarcar {self.quantidade_passageiros} passageiros')

c1 = Carro('Corsa', 4, 5)
print(c1.modelo)
c1.descrever()
