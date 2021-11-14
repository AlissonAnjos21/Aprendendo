# Verificando se algo é um objeto iterável
lista1 = [0, 1, 2, 3, 4, 5, 6]
lista2 = 'String'
naoLista = 12345

print(hasattr(lista1, '__iter__'))  # True
print(hasattr(lista2, '__iter__'))  # True
print(hasattr(naoLista, '__iter__'))  # False
