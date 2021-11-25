try:
    dicionario = {}
    # Ao invés de informar a chave, eu estou informando um índice númerico semelhante ao das listas/tuplas.
    print(dicionario[1])

except NameError as erro:
    print('Ocorreu um NameError ', erro)  # (Neste caso não será executado).

# Assim eu consigo tratar mais de um erro em determinada exceção.
except (KeyError, IndexError) as erro:
    print('Ocorreu um KeyError ou um IndexError ', erro)

except Exception as erro:
    print('Ocorreu um erro inesperado ', erro)  # (Neste caso não será executado).

print('Continuação do código')
