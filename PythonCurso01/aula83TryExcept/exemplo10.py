try:
    palavra = 'Palavrinha'
    print(palavra)

except NameError as erro:
    print('Ocorreu um NameError ', erro)  # (Neste caso não será executado).

except (KeyError, IndexError) as erro:
    print('Ocorreu um KeyError ou um IndexError ', erro)  # (Neste caso não será executado).

except Exception as erro:
    print('Ocorreu um erro inesperado ', erro)  # (Neste caso não será executado).

 # Eu consigo mesclar o uso do else e do finally, lembrando que o else só é executado caso o try seja executado com sucesso e o finally é executado independentemente de qualquer coisa.   
else:
    print('Não ocorreu nenhum erro :D')
    print(palavra)
finally:
    print('Executo independentemente de tudo')
    palavra = 'Vazio'

print('Continuação do código')
print(palavra)
