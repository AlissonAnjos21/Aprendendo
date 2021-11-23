# Gere uma lista que contenha um tupla com os nomes dos metais junto a um número que representa o seu índice.

from itertools import count

contador = count()
metais = ['Ferro', 'Chumbo', 'Cobre', 'Ouro', 'Prata', 'Estanho', 'Níquel', 'Alumínio']

resultado = list(zip(contador, metais))
print(resultado)
