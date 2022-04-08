from dataclasses import dataclass

# Quando o parâmetro frozen está ativado essa classe congela e se torna imutável, ou seja, eu não poderia editar o valor dos atributos, nem criar coisas.
@dataclass(frozen=True)
class Carro:
    modelo: str
    quantidade_portas: int
    quantidade_passageiros: int

c1 = Carro('Corsa', 4, 5)