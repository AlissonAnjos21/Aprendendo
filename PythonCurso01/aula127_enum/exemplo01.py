# O Enum é útil para filtrar itens que dizem respeito a determinado grupo a ser definido

from enum import Enum, auto

class Comida(Enum):
    # Auto equivale como se vc estivesse autoincrementando um número, começando do 1
    banana = auto()  # Neste caso, eu estou atribuindo um valor auto(), e como ele é o primeiro o valor será 1
    maca = auto()  # 2 (equivalente a colocar: maca = 2)
    melancia = auto()  # 3

def come(comida):
    if not isinstance(comida, Comida):
        raise ValueError('Você não deve fazer disso sua comida')
    return f'Comendo {comida.name}'

print(come(Comida.banana))
print(come(Comida.melancia))
print(come(Comida.maca))
# print(come('pneu'))  # Erro!

for comida in Comida:
    print(f'Comendo: {comida}\nNome da comida: {comida.name}\n"Id da comida:" {comida.value}')
