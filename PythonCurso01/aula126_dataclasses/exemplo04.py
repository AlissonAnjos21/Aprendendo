from dataclasses import dataclass

# Dentre os métodos já ativados estão: __init__(), __eq__(), __repr__(), etc
# Porém, é possível que eu desabilite esses métodos de veem embutidos nas dataclasses

@dataclass(eq=False, repr=False)
class Carro:
    modelo: str
    quantidade_portas: int
    quantidade_passageiros: int

c1 = Carro('Corsa', 4, 5)
c2 = Carro('Corsa', 4, 5)

print(c1 == c2)  # False
print(c1)  # <__main__.Carro object at 0x00000182BA13D9F0>
