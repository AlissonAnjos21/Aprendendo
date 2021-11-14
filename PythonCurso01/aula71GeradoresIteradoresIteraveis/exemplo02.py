# Verificando se algo é um objeto iterador

lista1 = [0, 1, 2, 3, 4, 5, 6]
print(hasattr(lista1, '__next__'))  # Embora ela seja um objeto iterável, ela não é um iterador (False)

lista2 = [0, 1, 2, 3, 4, 5]
lista2 = iter(lista2)  # Transformo a lista2 em um objeto iterador
print(hasattr(lista2, '__next__'))  # True

# Começa mostrando o primeiro item da lista e depois vai mostrar o próximo item da lista
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
