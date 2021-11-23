from itertools import count

# É possível falar de onde a função count começa a contar, como também quantos números ela pula.
# A função espera que o pulo seja um número inteiro, porém ela também funciona com números float.
contador = count(start=21, step=0.01)

for valor in contador:
    # A função round arredonda os números até a casa decimal informada
    print(round(valor, 2))
    if valor >=42:
        break
