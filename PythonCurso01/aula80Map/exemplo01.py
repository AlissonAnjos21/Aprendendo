# Utilizando a função map

from dados import produtos, pessoas, lista

# A função map usa de uma função para modificar a partir dela um objeto iterável, devolvendo assim um iterador.
vezes_dois = map(lambda x: x * 2, lista)
# Para visualizar os valores itere sobre ele ou converta-o para uma lista.
print(list(vezes_dois))

# Usando list comprehension também é possível, esse por sua vez retorna logo uma lista.
# vezes_2 = [x * 2 for x in lista]
# print(vezes_2)
