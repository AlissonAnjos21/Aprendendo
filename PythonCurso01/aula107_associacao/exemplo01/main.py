"""
Na relação de associação, as classes se comunicam entre si, porém uma classe não depende de outra para existir, ou seja, elas podem existir individualmente
"""

from classes import Agricultor
from classes import Enxada
from classes import Trator

agricultor = Agricultor('Joilson')
enxada = Enxada('Enxada rotatória')
trator = Trator()

print(agricultor.nome)  # Joilson
print(enxada.tipo)  # Enxada rotatória
enxada.arar()  # A enxada está arando o solo...
trator.arar()  # O trator está arando o solo...

# Consigo definir a ferramenta do agricultor como sendo uma instância de outra classe
agricultor.ferramenta = enxada

print(agricultor.ferramenta.tipo)  # Enxada rotatória
agricultor.ferramenta.arar()  # A enxada está arando o solo...
