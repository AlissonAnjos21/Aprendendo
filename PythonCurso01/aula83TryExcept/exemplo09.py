try:
    palavra = 'Palavrinha'
    print(palavra)

except NameError as erro:
    print('Ocorreu um NameError ', erro)  # (Neste caso não será executado).

except (KeyError, IndexError) as erro:
    print('Ocorreu um KeyError ou um IndexError ', erro)  # (Neste caso não será executado).

except Exception as erro:
    print('Ocorreu um erro inesperado ', erro)  # (Neste caso não será executado).

# Executará independentemente se o try foi executado com sucesso ou não.
finally:
    print('Executo independentemente de tudo')
    palavra = 'Vazio'

print('Continuação do código')
print(palavra)
