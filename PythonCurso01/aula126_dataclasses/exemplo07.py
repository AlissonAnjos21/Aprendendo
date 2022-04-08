from dataclasses import dataclass
from dataclasses import field

@dataclass()
class Contador:
    comeca: str
    termina: str = field(repr=False)  # Não mostrará o termina quando eu der print na instância

c1 = Contador(1, 21)
print(c1)
