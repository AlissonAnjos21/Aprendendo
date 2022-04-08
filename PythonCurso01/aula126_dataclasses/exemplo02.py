from dataclasses import dataclass

@dataclass
class Carro:
    modelo: str
    quantidade_portas: int
    quantidade_passageiros: int

    # O post_init inicia depois do init, mas como as dataclasses não possuem um init explicito, o post_init funciona após os atributos da classe serem definidos
    def __post_init__(self):
        self.porta_passageiro = f'{self.quantidade_portas} portas para {self.quantidade_passageiros} passageiros'

c1 = Carro('Corsa', 4, 5)
print(c1.porta_passageiro)
