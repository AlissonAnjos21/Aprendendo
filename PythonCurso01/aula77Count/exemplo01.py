# Função count

# Para usá-la é necessário importar essa função.
from itertools import count

# Enquanto a função range é um iterável, a função count é um iterador, sendo assim é possível usar a função next nela.
contador = count()
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
