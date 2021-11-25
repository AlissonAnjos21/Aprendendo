try:
    dicionario = {}
    # Ao invés de informar a chave, eu estou informando um índice númerico semelhante ao das listas/tuplas.
    print(dicionario[1])

except NameError as erro:
    print('Ocorreu um NameError ', erro)  # (Neste caso não será executado).

except KeyError as erro:
    print('Ocorreu um KeyError ', erro)

except IndexError as erro:
    print('Ocorreu um IndexError ', erro)  # (Neste caso não será executado).

except Exception as erro:
    print('Ocorreu um erro inesperado ', erro)  # (Neste caso não será executado).

print('Continuação do código')
