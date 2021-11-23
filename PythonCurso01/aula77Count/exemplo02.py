from itertools import count

contador = count()

# Essa função não tem fim, então cuidado com o looping infinito que ela possívelmente pode ocasionar.
for valor in contador:
    print(valor)
    # Para previnir isso é possível usar condições.
    if valor >= 21:
        break
