try:
    print(1/0)
    
except NameError:
    print('Ocorreu um NameError')  # (Neste caso não será executado).

# Para prevenir possíveis erros inesperados usa-se isto (Neste caso eu estou tentando dividir um número por zero e o unico erro que eu esperava era o NameError).
# Salvei o erro inesperado em "erro".
except Exception as erro:
    print('Ocorreu um erro inesperado', erro)

print('Continuação do código')
