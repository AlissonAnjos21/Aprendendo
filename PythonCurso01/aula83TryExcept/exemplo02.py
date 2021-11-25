try:
    print(ola)
# Nesse caso apenas caso ocorra um erro específico ele irá até o except (Nesse caso o NameError).
except NameError as erro:
    print('Erro de Nome')