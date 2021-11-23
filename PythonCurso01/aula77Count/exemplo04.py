from itertools import count

# Também é possível fazer ele contar para trás
contador = count(start=21, step=-1)

for valor in contador:
    print(valor)
    if valor <= 0:
        break
    