from dataclasses import dataclass
from dataclasses import asdict, astuple

@dataclass()
class Contador:
    comeca: str
    termina: str

c1 = Contador(1, 21)

# Transforma os atributos da classe em itens de um dicionário
print(asdict(c1))  # {'comeca': 1, 'termina': 21}

# Transforma os valores dos atributos da classe em itens de uma tupla
print(astuple(c1))  # (1, 21)
