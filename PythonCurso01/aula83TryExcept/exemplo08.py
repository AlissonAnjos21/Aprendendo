try:
    palavra = 'Palavra'
    print(palavra)

except NameError as erro:
    print('Ocorreu um NameError ', erro)  # (Neste caso não será executado).

except (KeyError, IndexError) as erro:
    print('Ocorreu um KeyError ou um IndexError ', erro)  # (Neste caso não será executado).

except Exception as erro:
    print('Ocorreu um erro inesperado ', erro)  # (Neste caso não será executado).

# Executará caso o try seja executado com sucesso, ou seja, caso não ocorra nenhum erro.
else:
    print('Não ocorreu nenhum erro :D')

print('Continuação do código')
