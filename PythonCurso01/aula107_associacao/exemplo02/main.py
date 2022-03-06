from classes import Agricultor
from classes import Enxada
from classes import Trator

agricultor = Agricultor('Rubens')
enxada = Enxada('Enxada de Ponta Fina')
trator = Trator()

agricultor.ferramenta = trator
agricultor.ferramenta.arar()

del agricultor  # Apago a instância agricultor

# Gera um erro, pois o agricultor foi deletado
# print(agricultor.nome) 

trator.arar()  # Funciona normalmente, pois esta é uma classe independente da instância agricultor
