from enum import Enum, auto

class Comida(Enum):
    banana = auto()
    maca = auto()
    melancia = auto()

for comida in Comida:
    print(f'Comendo: {comida}\nNome da comida: {comida.name}\n"Id" da comida: {comida.value}\n')
