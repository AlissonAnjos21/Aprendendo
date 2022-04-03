"""Dicas interessantes sobre typehints

Ele em si não faz nada, porém é algo bastante útil para aquelas pessoa que forem ler o seu código
Link da documentação do Python sobre Typing: https://docs.python.org/3/library/typing.html 
"""

x: int = 21
y: float = 21.21
z: str = 'Vinte e um'

# Informando o tipo dos parâmetros
def funcao_1(x: int, y: float, z: str):
    return x, y, z

# Informando o tipo do retorno da função
def funcao_2() -> float:
    return 21.21

# Informando o tipo de retorno quando não se sabe ao certo o tipo a ser retornado
from typing import Union
def funcao_3(x: int) -> Union[list, dict]:
    if x <= 0:
        return [1, 2, 3]
    return {1: 'Um', 2: 'Dois', 3: 'Três'} 
