from dataclasses import dataclass

# Dentre os métodos já ativados estão: __init__(), __eq__(), __repr__(), etc

@dataclass
class Carro:
    modelo: str
    quantidade_portas: int
    quantidade_passageiros: int

c1 = Carro('Corsa', 4, 5)
c2 = Carro('Corsa', 4, 5)

# Método __eq__ já embutido:
print(c1 == c2)  # True

# Metodo __repr__ já embutido:
print(c1)  # Carro(modelo='Corsa', quantidade_portas=4, quantidade_passageiros=5)
