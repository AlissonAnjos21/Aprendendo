"""
Um gerador usa a mesma lógia do objeto iterador, ele vai apenas mostrar o item que você pediu.
Isso é bastante útil pois não consome memória desnecessária abrigando itens desnecessários, a memória guardará apenas o valor requerido.
"""
import sys

lista1 = [x for x in range(10000)]
lista2 = (x for x in range(10000))

print(type(lista1))  # Lista comum
print(type(lista2))  # Gerador

print(sys.getsizeof(lista1))  # Consome 85176 bytes
print(sys.getsizeof(lista2))  # Consome 112 bytes

# É possível iterar em ambas

# for v in lista1:
#     print(v)

# for v in lista2:
#     print(v)

