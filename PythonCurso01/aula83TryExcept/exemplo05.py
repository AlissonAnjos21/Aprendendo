try:
    lista = []
    # Pedindo um índice que não existe.
    print(lista[1])

except NameError as erro:
    print('Ocorreu um NameError', erro)  # (Neste caso não será executado).

# Como eu pedi um índice que não existe, ele cairá neste laço de IndexError.
except IndexError as erro:
    print('Ocorreu um IndexError', erro)

except Exception as erro:
    print('Ocorreu um erro inesperado', erro)  # (Neste caso não será executado).

print('Continuação do código')
