# Some os valores de duas listas retornando uma terceira lista como resultado.
# Só deverá ser somado até o ultimo valor da menor lista.

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

lista_resultado = [x + y for x, y in zip(lista1, lista2)]
print(lista_resultado)

# Agora, devererão ser somados todos os valores.

from itertools import zip_longest

lista_novo_resultado = [x + y for x, y in zip_longest(lista1, lista2, fillvalue=0)]
print(lista_novo_resultado)
